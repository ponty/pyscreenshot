import logging
import os

from PIL import Image

from pyscreenshot.plugins.backend import UNKNOWN_VERSION, CBackend

log = logging.getLogger(__name__)


class KdeDBusError(Exception):
    pass


class KwinDBusWrapper(CBackend):
    name = "kwin_dbus"
    is_subprocess = True

    def grab(self, bbox=None):
        has_jeepney = False
        try:
            from jeepney.wrappers import MessageGenerator, new_method_call
            from jeepney import new_method_call
            from jeepney.integrate.blocking import connect_and_authenticate

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
        connection = connect_and_authenticate(bus="SESSION")
        dbscr = Screenshot()
        # bbox not working:
        #   if bbox: msg = dbscr.screenshotArea(bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1], False)
        msg = dbscr.screenshotFullscreen(False)
        filename = connection.send_and_get_reply(msg)
        filename = filename[0]
        if not filename:
            raise KdeDBusError()

        im = Image.open(filename)
        os.remove(filename)
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return UNKNOWN_VERSION
