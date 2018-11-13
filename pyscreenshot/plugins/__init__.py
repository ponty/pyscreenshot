

import sys

from pyscreenshot.plugins import wxscreen, gtkpixbuf, qt4grabwindow, qt5grabwindow, \
    scrot, imagemagick, mac_quartz, mac_screencapture, pil, pyside_grabwindow, \
    gnome_screenshot, gdk3pixbuf

if sys.platform == 'linux2':
    BACKENDS = [
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        gdk3pixbuf.Gdk3PixbufWrapper,
        qt4grabwindow.Qt4GrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
        pyside_grabwindow.PySideGrabWindow,
        gnome_screenshot.GnomeScreenshotWrapper,
    ]
elif sys.platform == 'darwin':
    BACKENDS = [
        mac_quartz.MacQuartzWrapper,
        mac_screencapture.ScreencaptureWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        gdk3pixbuf.Gdk3PixbufWrapper,
        qt4grabwindow.Qt4GrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
        pyside_grabwindow.PySideGrabWindow,
    ]
elif sys.platform == 'win32':
    BACKENDS = [
        pil.PilWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        gdk3pixbuf.Gdk3PixbufWrapper,
        qt4grabwindow.Qt4GrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
        pyside_grabwindow.PySideGrabWindow,
    ]
else:
    BACKENDS = [
        pil.PilWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        gdk3pixbuf.Gdk3PixbufWrapper,
        qt4grabwindow.Qt4GrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
        mac_screencapture.ScreencaptureWrapper,
        mac_quartz.MacQuartzWrapper,
        pyside_grabwindow.PySideGrabWindow,
        gnome_screenshot.GnomeScreenshotWrapper,
    ]


default_preference = [x.name for x in BACKENDS]
