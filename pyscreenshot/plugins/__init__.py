

import sys

from pyscreenshot.plugins import wxscreen, gtkpixbuf, qt4grabwindow, qt5grabwindow, \
    scrot, imagemagick, mac_quartz, mac_screencapture, pil, pyside_grabwindow, pyside2_grabwindow, qtpy_grabwindow, \
    gnome_screenshot, gdk3pixbuf

_qt_backends = [
    qtpy_grabwindow.QtPyGrabWindow,
    qt5grabwindow.Qt5GrabWindow,
    qt4grabwindow.Qt4GrabWindow,
    pyside2_grabwindow.PySide2GrabWindow,
    pyside_grabwindow.PySideGrabWindow,
]

# external processes (scrot,imagemagick) are more safe (less conflicts) than library calls.
if sys.platform.startswith('linux'):
    BACKENDS = [
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,

    ]+_qt_backends+[

        wxscreen.WxScreen,
        gdk3pixbuf.Gdk3PixbufWrapper,
        gtkpixbuf.GtkPixbufWrapper,

        gnome_screenshot.GnomeScreenshotWrapper,
    ]
elif sys.platform == 'darwin':
    BACKENDS = [
        pil.PilWrapper,

        mac_screencapture.ScreencaptureWrapper,
        mac_quartz.MacQuartzWrapper,

        # scrot.ScrotWrapper,
        # imagemagick.ImagemagickWrapper,

    ]+_qt_backends+[

        wxscreen.WxScreen,
        gdk3pixbuf.Gdk3PixbufWrapper,
        # gtkpixbuf.GtkPixbufWrapper,
    ]
elif sys.platform == 'win32':
    BACKENDS = [
        pil.PilWrapper,

    ]+_qt_backends+[
        gtkpixbuf.GtkPixbufWrapper,

        wxscreen.WxScreen,
        gdk3pixbuf.Gdk3PixbufWrapper,

        # scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
    ]
else:
    BACKENDS = [
        pil.PilWrapper,

        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,

    ]+_qt_backends+[

        wxscreen.WxScreen,
        gdk3pixbuf.Gdk3PixbufWrapper,
        gtkpixbuf.GtkPixbufWrapper,

        mac_screencapture.ScreencaptureWrapper,
        mac_quartz.MacQuartzWrapper,

        gnome_screenshot.GnomeScreenshotWrapper,
    ]


default_preference = [x.name for x in BACKENDS]
