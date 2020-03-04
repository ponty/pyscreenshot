from PIL import __version__
from pyscreenshot.plugins.backend import CBackend


class PilWrapper(CBackend):

    """windows only."""

    name = "pil"
    childprocess = False

    def __init__(self):
        from PIL import ImageGrab  # windows and osx only

        self.ImageGrab = ImageGrab

    def grab(self, bbox=None):
        return self.ImageGrab.grab(bbox)

    def backend_version(self):
        return __version__
