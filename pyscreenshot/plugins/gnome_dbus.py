import logging

from pyscreenshot.plugins.backend import UNKNOWN_VERSION, CBackend
from pyscreenshot.tempexport import read_func_img

log = logging.getLogger(__name__)


class GnomeDBusError(Exception):
    pass


class GnomeDBusWrapper(CBackend):
    name = "gnome_dbus"
    is_subprocess = True

    def grab(self, bbox=None):
        im = read_func_img(self._grab_to_file, bbox)
        return im

    def _grab_to_file(self, filename, bbox=None):
        has_jeepney = False
        try:
            from jeepney.wrappers import MessageGenerator, new_method_call
            from jeepney import new_method_call
            from jeepney.integrate.blocking import connect_and_authenticate

            has_jeepney = True
        except ImportError:
            pass

        if not has_jeepney:
            raise GnomeDBusError("jeepney library is missing")

        class Screenshot(MessageGenerator):
            interface = "org.gnome.Shell.Screenshot"

            def __init__(
                self,
                object_path="/org/gnome/Shell/Screenshot",
                bus_name="org.gnome.Shell.Screenshot",
            ):
                super().__init__(object_path=object_path, bus_name=bus_name)

            def Screenshot(self, include_cursor, flash, filename):
                return new_method_call(
                    self, "Screenshot", "bbs", (include_cursor, flash, filename)
                )

            def ScreenshotArea(self, x, y, width, height, flash, filename):
                return new_method_call(
                    self,
                    "ScreenshotArea",
                    "iiiibs",
                    (x, y, width, height, flash, filename),
                )

        # https://jeepney.readthedocs.io/en/latest/integrate.html
        connection = connect_and_authenticate(bus="SESSION")
        dbscr = Screenshot()
        if bbox:
            msg = dbscr.ScreenshotArea(
                bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1], False, filename,
            )
        else:
            msg = dbscr.Screenshot(False, False, filename)
        result = connection.send_and_get_reply(msg)
        if not result[0]:
            raise GnomeDBusError("dbus error: %s %s" % (msg, result))

    def backend_version(self):
        return UNKNOWN_VERSION
