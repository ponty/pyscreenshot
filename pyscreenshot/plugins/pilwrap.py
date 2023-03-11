from PIL import __version__

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.util import use_x_display


class PilWrapper(CBackend):
    name = "pil"

    def grab(self, bbox=None):
        from PIL import ImageGrab

        # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
        # On Linux, if xdisplay is None then gnome-screenshot will be used if it is installed.
        # To capture the default X11 display instead, pass xdisplay=""
        xdisplay = None
        if use_x_display():
            xdisplay = ""
        return ImageGrab.grab(bbox, xdisplay=xdisplay)

    def backend_version(self):
        return __version__
