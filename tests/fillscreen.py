import atexit
import logging
import tempfile
from os.path import join
from shutil import rmtree
from time import sleep

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from PIL import Image

import pyscreenshot
from pyscreenshot.util import platform_is_osx, platform_is_win
from size import display_size

log = logging.getLogger(__name__)

refimgpath = None


class FillscreenError(Exception):
    pass


def generate_image():
    w, h = display_size()
    log.debug("display size: %s x %s", w, h)
    if w <= 0 or h <= 0:
        raise ValueError("invalid display size %s x %s" % (w, h))
    img = Image.new("RGB", (w, h), "black")  # Create a new black image
    pixels = img.load()  # Create the pixel map
    i = 0
    B = 42
    for x in range(img.size[0]):  # For every pixel:
        for y in range(img.size[1]):
            r = int(x * 255 / w)
            g = int(y * 255 / h)

            b = int(((x % B) * 255 / B + (y % B) * 255 / B) / 2)
            pixels[x, y] = (r, g, b)  # Set the colour accordingly
            i += 1
    return img


def init():
    global refimgpath
    if not refimgpath:
        d = tempfile.mkdtemp(prefix="fillscreen")
        atexit.register(lambda: rmtree(d))
        refimgpath = join(d, "ref.png")

        im = generate_image()
        im.save(refimgpath)

        if platform_is_win():
            cmd = [
                "C:\\Program Files (x86)\\FastStone Image Viewer\\FSViewer.exe",
                refimgpath,
            ]
        else:
            cmd = [
                "pqiv",
                "--fullscreen",
                "--hide-info-box",
                "--disable-scaling",
                refimgpath,
            ]
        proc = EasyProcess(cmd).start()
        atexit.register(proc.stop)
        print(refimgpath)
        sleep(5)  # wait for image displayed
        if not proc.is_alive():
            raise FillscreenError("pqiv stopped: %s" % proc)

        # if the OS has color correction
        #  then the screenshot has slighly different color than the original image
        if platform_is_win() or platform_is_osx():
            refimgpath = refimgpath + ".pil.png"
            im = pyscreenshot.grab(backend="pil")
            im.save(refimgpath)
            log.debug("%s saved", refimgpath)

    return refimgpath


@entrypoint
def main(saveimage=""):
    im = generate_image()
    im.show()
