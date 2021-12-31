import atexit
import logging
import sys
import tempfile
from os.path import dirname, join
from shutil import rmtree
from time import sleep

from easyprocess import EasyProcess

import pyscreenshot
from genimg import generate_image
from pyscreenshot.util import platform_is_osx, platform_is_win

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

        im = generate_image()
        im.save(refimgpath)

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
        print(refimgpath)
        sleep(40)  # TODO: wait for image displayed
        if not proc.is_alive():
            raise FillscreenError("fillscreen stopped: %s" % proc)

        # if the OS has color correction
        #  then the screenshot has slighly different color than the original image
        if platform_is_win() or platform_is_osx():
            refimgpath = refimgpath + ".pil.png"
            im = pyscreenshot.grab(backend="pil")
            im.save(refimgpath)
            log.debug("%s saved", refimgpath)

    return refimgpath
