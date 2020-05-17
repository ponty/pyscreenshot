import logging
import traceback

from pyscreenshot.childproc import childprocess_grab
from pyscreenshot.err import FailedBackendError
from pyscreenshot.plugins import backend_dict
from pyscreenshot.plugins.gdk3pixbuf import Gdk3PixbufWrapper
from pyscreenshot.plugins.gnome_dbus import GnomeDBusWrapper
from pyscreenshot.plugins.gnome_screenshot import GnomeScreenshotWrapper
from pyscreenshot.plugins.gtkpixbuf import GtkPixbufWrapper
from pyscreenshot.plugins.imagemagick import ImagemagickWrapper
from pyscreenshot.plugins.kwin_dbus import KwinDBusWrapper
from pyscreenshot.plugins.mac_quartz import MacQuartzWrapper
from pyscreenshot.plugins.mac_screencapture import ScreencaptureWrapper
from pyscreenshot.plugins.maim import MaimWrapper
from pyscreenshot.plugins.msswrap import MssWrapper
from pyscreenshot.plugins.pilwrap import PilWrapper
from pyscreenshot.plugins.pyside2_grabwindow import PySide2GrabWindow
from pyscreenshot.plugins.pyside_grabwindow import PySideGrabWindow
from pyscreenshot.plugins.qt4grabwindow import Qt4GrabWindow
from pyscreenshot.plugins.qt5grabwindow import Qt5GrabWindow
from pyscreenshot.plugins.qtpy_grabwindow import QtPyGrabWindow
from pyscreenshot.plugins.scrot import ScrotWrapper
from pyscreenshot.plugins.wxscreen import WxScreen
from pyscreenshot.util import (
    platform_is_linux,
    platform_is_osx,
    platform_is_win,
    use_x_display,
)

log = logging.getLogger(__name__)


log = logging.getLogger(__name__)


def qt():
    yield QtPyGrabWindow
    yield Qt5GrabWindow
    yield Qt4GrabWindow
    yield PySide2GrabWindow
    yield PySideGrabWindow


def backends(childprocess):
    if platform_is_linux():
        if use_x_display():
            if childprocess:
                # scrot is 2x faster than mss
                yield ScrotWrapper
                yield MssWrapper
            else:
                # mss is 6x faster than scrot
                yield MssWrapper
                yield ScrotWrapper
            yield MaimWrapper
            yield ImagemagickWrapper
            yield Gdk3PixbufWrapper
            yield WxScreen
            yield GtkPixbufWrapper
            for x in qt():
                yield x
        yield GnomeDBusWrapper

        # on screen notification
        yield KwinDBusWrapper

        # flash effect
        yield GnomeScreenshotWrapper

    elif platform_is_osx():
        # first check for X
        if use_x_display():
            pass
        else:
            # fast
            yield MssWrapper

            # latest version should work
            yield PilWrapper

            # alternatives for older pillow versions
            yield ScreencaptureWrapper
            yield MacQuartzWrapper

            # qt has some color difference

            # does not work: Gdk3, wx, Imagemagick

    elif platform_is_win():
        # fast
        yield MssWrapper

        yield PilWrapper
    else:
        for x in backend_dict.values():
            yield x


def select_childprocess(childprocess, backend_class):
    if backend_class.is_subprocess:
        # backend is always a subprocess -> nothing to do
        return False

    return childprocess


def auto(bbox, childprocess):
    im = None
    for backend_class in backends(childprocess):
        backend_name = backend_class.name
        try:
            if select_childprocess(childprocess, backend_class):
                log.debug('running "%s" in child process', backend_name)
                im = childprocess_grab(backend_name, bbox)
            else:
                obj = backend_class()

                im = obj.grab(bbox)
            break
        except Exception:
            msg = traceback.format_exc()
            log.debug(msg)
    if not im:
        msg = "All backends failed!"
        raise FailedBackendError(msg)

    return im


def force(backend_name, bbox, childprocess):
    backend_class = backend_dict[backend_name]
    if select_childprocess(childprocess, backend_class):
        log.debug('running "%s" in child process', backend_name)
        return childprocess_grab(backend_name, bbox)
    else:
        obj = backend_class()
        im = obj.grab(bbox)
        return im


def backend_grab(backend, bbox, childprocess):
    if backend:
        return force(backend, bbox, childprocess)
    else:
        return auto(bbox, childprocess)


def backend_version2(backend_name):
    backend_class = backend_dict[backend_name]
    obj = backend_class()
    v = obj.backend_version()
    return v
