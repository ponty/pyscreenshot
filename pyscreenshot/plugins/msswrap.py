# import atexit
import sys

from PIL import Image

# https://python-mss.readthedocs.io/examples.html

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
PY_MINOR = sys.version_info[1]


class MssError(Exception):
    pass


sct = None

# TODO: not working without xrandr extension
# only bits_per_pixel == 32 is supported


class MssWrapper(object):
    name = "mss"
    childprocess = False

    def __init__(self):
        if PY2:
            raise MssError()
        if PY3:
            if PY_MINOR < 5:
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
