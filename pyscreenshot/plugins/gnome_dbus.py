import logging

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import read_func_img

log = logging.getLogger(__name__)


class GnomeDBusError(Exception):
    pass


class GnomeDBusWrapper(CBackend):
    name = "gnome_dbus"
    childprocess = True

    def __init__(self):
        import dbus  # TODO: use pure dbus lib

        self.dbus = dbus

    def grab(self, bbox=None):
        im = read_func_img(self._grab_to_file, bbox)
        return im

    def _grab_to_file(self, filename, bbox=None):
        bus = self.dbus.SessionBus()
        proxy = bus.get_object("org.gnome.Shell", "/org/gnome/Shell/Screenshot")
        dbus_interface = "org.gnome.Shell.Screenshot"
        if bbox:
            ok, _ = proxy.ScreenshotArea(
                bbox[0],
                bbox[1],
                bbox[2] - bbox[0],
                bbox[3] - bbox[1],
                False,
                filename,
                dbus_interface=dbus_interface,
            )
        else:
            ok, _ = proxy.Screenshot(
                False, False, filename, dbus_interface=dbus_interface
            )
        if not ok:
            raise GnomeDBusError()

    def backend_version(self):
        return None  # TODO
