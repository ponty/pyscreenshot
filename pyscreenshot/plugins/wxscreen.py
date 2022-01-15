import logging

from PIL import Image

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.util import platform_is_osx

log = logging.getLogger(__name__)

# based on:
# http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux


class WxBackendError(Exception):
    pass


app = None


class WxScreen(CBackend):
    name = "wx"
    # conflict with pygdk3
    #  wx is never installed by default
    # pygdk3 is default on Gnome

    def grab(self, bbox=None):
        if platform_is_osx():
            raise WxBackendError("osx not supported")
        import wx  # type: ignore

        global app
        if not app:
            app = wx.App()
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
            im.frombytes(bytes(myWxImage.GetData()))
        else:
            # for PIL
            im.fromstring(myWxImage.GetData())
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        import wx

        return wx.__version__
