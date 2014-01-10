import gtkpixbuf
import imagemagick
import pil
import qtgrabwindow
import scrot
import wxscreen
import mac_screencapture


BACKENDS = [
    pil.PilWrapper,
    scrot.ScrotWrapper,
    wxscreen.WxScreen,
    gtkpixbuf.GtkPixbufWrapper,
    qtgrabwindow.QtGrabWindow,
    imagemagick.ImagemagickWrapper,
    mac_screencapture.ScreencaptureWrapper,
]

default_preference = [x.name for x in BACKENDS]
