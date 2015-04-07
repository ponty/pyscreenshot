import gtkpixbuf
import imagemagick
import pil
import qtgrabwindow
import scrot
import wxscreen
import mac_screencapture
import mac_quartz
import sys


if sys.platform == 'linux2':
    BACKENDS = [
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
    ]
elif sys.platform == 'darwin':
    BACKENDS = [
        mac_quartz.MacQuartzWrapper,
        mac_screencapture.ScreencaptureWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
    ]
elif sys.platform == 'win32':
    BACKENDS = [
        pil.PilWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
    ]
else:
    BACKENDS = [
        pil.PilWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
        mac_screencapture.ScreencaptureWrapper,
        mac_quartz.MacQuartzWrapper,
    ]


default_preference = [x.name for x in BACKENDS]
