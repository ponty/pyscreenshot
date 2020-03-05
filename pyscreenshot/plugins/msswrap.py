# import atexit

from PIL import Image
from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.util import py2, py3, py_minor

# https://python-mss.readthedocs.io/examples.html


class MssError(Exception):
    pass


sct = None

# TODO: not working without xrandr extension
# only bits_per_pixel == 32 is supported


class MssWrapper(CBackend):
    name = "mss"
    childprocess = False

    def __init__(self):
        if py2():
            raise MssError()
        if py3():
            if py_minor() < 5:
                raise MssError()
        import mss

        self.mss = mss
        # atexit.register(sct.close())

    def grab(self, bbox=None):
        global sct
        if not sct:
            sct = self.mss.mss()

        # with self.mss.mss() as sct:
        if bbox:
            monitor = bbox
        else:
            monitor = sct.monitors[0]
        sct_img = sct.grab(monitor)

        im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        # The same, but less efficient:
        # im = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        return im

    def backend_version(self):
        import mss

        return mss.__version__
