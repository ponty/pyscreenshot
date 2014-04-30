import gtkpixbuf
import imagemagick
import pil
import qtgrabwindow
import scrot
import wxscreen
import mac_screencapture
import mac_quartz


BACKENDS = [
    pil.PilWrapper,
    scrot.ScrotWrapper,
    wxscreen.WxScreen,
    gtkpixbuf.GtkPixbufWrapper,
    qtgrabwindow.QtGrabWindow,
    imagemagick.ImagemagickWrapper,
    mac_screencapture.ScreencaptureWrapper,
    mac_quartz.MacQuartzWrapper,
]

default_preference = [x.name for x in BACKENDS]
