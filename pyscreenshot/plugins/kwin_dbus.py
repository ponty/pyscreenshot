import logging
import os

from PIL import Image

from pyscreenshot.plugins.backend import UNKNOWN_VERSION, CBackend

log = logging.getLogger(__name__)


class KdeDBusError(Exception):
    pass


# https://gitlab.gnome.org/GNOME/gimp/-/issues/6626
# The org.kde.kwin.Screenshot interface is deprecated in KDE Plasma 5.22.

# "The process is not authorized to take a screenshot"


class KwinDBusWrapper(CBackend):
    name = "kwin_dbus"
    is_subprocess = True

    def grab(self, bbox=None):
        has_jeepney = False
        try:
            # from jeepney import new_method_call
            from jeepney.io.blocking import open_dbus_connection  # type: ignore
            from jeepney.wrappers import MessageGenerator  # type: ignore
            from jeepney.wrappers import new_method_call

            has_jeepney = True
        except ImportError:
            pass

        if not has_jeepney:
            raise KdeDBusError("jeepney library is missing")

        class Screenshot(MessageGenerator):
            interface = "org.kde.kwin.Screenshot"

            def __init__(self, object_path="/Screenshot", bus_name="org.kde.KWin"):
                super().__init__(object_path=object_path, bus_name=bus_name)

            def screenshotFullscreen(self, captureCursor):
                return new_method_call(
                    self, "screenshotFullscreen", "b", (captureCursor,)
                )

            def screenshotArea(self, x, y, width, height, captureCursor):
                return new_method_call(
                    self,
                    "screenshotArea",
                    "iiiib",
                    (x, y, width, height, captureCursor),
                )

        # https://jeepney.readthedocs.io/en/latest/integrate.html
        connection = open_dbus_connection(bus="SESSION")
        dbscr = Screenshot()
        # bbox not working:
        #   if bbox: msg = dbscr.screenshotArea(bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1], False)
        msg = dbscr.screenshotFullscreen(False)
        reply = connection.send_and_get_reply(msg)
        filename = reply.body[0]
        if not filename:
            raise KdeDBusError()

        im = Image.open(filename)
        os.remove(filename)
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return UNKNOWN_VERSION
