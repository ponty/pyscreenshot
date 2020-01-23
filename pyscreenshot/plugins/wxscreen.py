import logging
import sys

from PIL import Image

PY2 = sys.version_info[0] == 2
if PY2:
    to_bytes = buffer
else:
    to_bytes = bytes
log = logging.getLogger(__name__)

# based on:
# http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux


class WxBackendError(Exception):
    pass


class WxScreen(object):
    name = "wx"
    childprocess = False

    def __init__(self):
        if sys.platform == "darwin":
            raise WxBackendError("osx not supported")  # TODO
        import wx

        self.wx = wx
        self.app = None

    def grab(self, bbox=None):
        wx = self.wx
        if not self.app:
            self.app = wx.App()
        screen = wx.ScreenDC()
        size = screen.GetSize()
        if wx.__version__ >= "4":
            bmp = wx.Bitmap(size[0], size[1])
        else:
            bmp = wx.EmptyBitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem
        if hasattr(bmp, "ConvertToImage"):
            myWxImage = bmp.ConvertToImage()
        else:
            myWxImage = wx.ImageFromBitmap(bmp)
        im = Image.new("RGB", (myWxImage.GetWidth(), myWxImage.GetHeight()))
        if hasattr(Image, "frombytes"):
            # for Pillow
            im.frombytes(to_bytes(myWxImage.GetData()))
        else:
            # for PIL
            im.fromstring(myWxImage.GetData())
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return self.wx.__version__
