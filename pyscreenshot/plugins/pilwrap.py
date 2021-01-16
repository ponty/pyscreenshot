from PIL import __version__

from pyscreenshot.plugins.backend import CBackend


class PilWrapper(CBackend):
    """Windows/MacOS only."""

    name = "pil"

    def grab(self, bbox=None):
        from PIL import ImageGrab  # windows and osx only

        return ImageGrab.grab(bbox)

    def backend_version(self):
        return __version__
