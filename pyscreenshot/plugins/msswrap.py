# import atexit

from PIL import Image

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.util import py_minor

# https://python-mss.readthedocs.io/examples.html


class MssError(Exception):
    pass


sct = None

# not working without xrandr extension
# only bits_per_pixel == 32 is supported


class MssWrapper(CBackend):
    name = "mss"

    def grab(self, bbox=None):
        if py_minor() < 5:
            raise MssError()
        import mss

        # atexit.register(sct.close())

        global sct
        if not sct:
            sct = mss.mss()

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
