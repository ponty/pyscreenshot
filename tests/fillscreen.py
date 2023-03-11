import atexit
import logging
import sys
import tempfile
from os.path import dirname, join
from shutil import rmtree
from time import sleep

from easyprocess import EasyProcess
from PIL import Image, ImageChops

import pyscreenshot
from pyscreenshot.util import platform_is_osx, platform_is_win

# from image_debug import ImageDebug


log = logging.getLogger(__name__)

refimgpath = None


class FillscreenError(Exception):
    pass


def init():
    global refimgpath
    if not refimgpath:
        d = tempfile.mkdtemp(prefix="fillscreen")
        atexit.register(lambda: rmtree(d))
        refimgpath = join(d, "ref.bmp")

        # img_ref = generate_image()
        # img_ref.save(refimgpath)

        # fillscreen_tk = join(dirname(__file__), "fillscreen_tk.py")
        fillscreen_pygame = join(dirname(__file__), "fillscreen_pygame.py")
        python = sys.executable
        cmd = [python, fillscreen_pygame, "--image", refimgpath]
        cmd += ["--debug"]
        # if platform_is_win():
        #     cmd = [
        #         "C:\\Program Files (x86)\\FastStone Image Viewer\\FSViewer.exe",
        #         refimgpath,
        #     ]
        # else:
        #     cmd = [
        #         "pqiv",
        #         "--fullscreen",
        #         "--hide-info-box",
        #         "--disable-scaling",
        #         refimgpath,
        #     ]
        # if platform_is_osx():
        #     cmd = [
        #         "pqiv",
        #         "--fullscreen",
        #         "--hide-info-box",
        #         "--disable-scaling",
        #         refimgpath,
        #     ]
        # else:
        #     cmd = [python, fillscreen_pygame, "--image", refimgpath]
        proc = EasyProcess(cmd).start()
        atexit.register(proc.stop)
        log.debug(refimgpath)

        # sleep(30)
        # imdbg = ImageDebug()
        t = 0
        while True:
            sleep(2)
            t += 2
            if t > 90:
                raise FillscreenError("fillscreen timeout: %s" % t)

            if not proc.is_alive():
                raise FillscreenError("fillscreen stopped: %s" % proc)

            try:
                img_ref = Image.open(refimgpath)
            except FileNotFoundError:
                continue
            im = pyscreenshot.grab()
            # imdbg.img_debug(im, "raw")
            im = im.convert("RGB")
            img_diff = ImageChops.difference(img_ref, im)
            ex = img_diff.getextrema()
            log.debug("diff getextrema: %s", ex)
            color_diff_max = max([b for (_, b) in ex])
            diff_bbox = img_diff.getbbox()
            if diff_bbox is not None:
                log.debug(
                    "different image data. color_diff_max:%s extrema:%s diff_bbox=%s"
                    % (color_diff_max, ex, diff_bbox)
                )
                # imdbg.img_debug(img_ref, "ref")
                # imdbg.img_debug(im, "got")
                # imdbg.img_debug(img_diff, "img_diff" + str(diff_bbox))

            if color_diff_max < 10:
                break

        # if the OS has color correction
        #  then the screenshot has slightly different color than the original image
        if platform_is_win() or platform_is_osx():
            refimgpath = refimgpath + ".pil.png"
            im = pyscreenshot.grab(backend="pil")
            im.save(refimgpath)
            log.debug("%s saved", refimgpath)

    return refimgpath
