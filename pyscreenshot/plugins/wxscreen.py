from PIL import Image
import logging

log = logging.getLogger(__name__)

class WxScreen(object):

    '''based on: http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux
    '''
    name = 'wx'
    childprocess = False

    def __init__(self):
        import wx
        self.wx = wx
        self.app = None

    def grab(self, bbox=None):
        wx = self.wx
        if not self.app:
            self.app = wx.App()
        screen = wx.ScreenDC()
        size = screen.GetSize()
        #Deprecated wx.EmptyBitmap()
        #bmp = wx.EmptyBitmap(size[0], size[1])
        bmp = wx.Bitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem
        #Deprecated wx.ImageFromBitmap()
        #myWxImage = wx.ImageFromBitmap(bmp)
        myWxImage = bmp.ConvertToImage()
        im = Image.new('RGB', (myWxImage.GetWidth(), myWxImage.GetHeight()))
        if hasattr(Image, 'frombytes'):
            # for Pillow
            '''Under Arch Linux, using Python 3 and wxpython installed with pip3
            Any call to pyscreenshot.grab() would return a: 
                TypeError: argument 1 must be read-only bytes-like object, not bytearray.
            Therefore, adding bytes() to convert myWxImage.GetData() from bytearray to bytes'''
            im.frombytes( bytes( myWxImage.GetData()))
        else:
            # for PIL
            im.fromstring(myWxImage.GetData())
        if bbox:
            im = im.crop(bbox)
        return im

    def grab_to_file(self, filename, bbox=None):
        # bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
        im = self.grab(bbox)
        im.save(filename)

    def backend_version(self):
        return self.wx.__version__
