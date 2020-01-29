from PIL import __version__


class PilWrapper(object):

    """windows only."""

    name = "pil"
    childprocess = False

    def __init__(self):
        from PIL import ImageGrab  # windows only

        self.ImageGrab = ImageGrab

    def grab(self, bbox=None):
        return self.ImageGrab.grab(bbox)

    def backend_version(self):
        return __version__
