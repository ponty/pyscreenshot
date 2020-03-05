import logging

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import read_func_img

# from jeepney.wrappers import MessageGenerator, new_method_call
# from jeepney import DBusAddress, new_method_call
# from jeepney.integrate.blocking import connect_and_authenticate


# class Screenshot(MessageGenerator):
#     interface = "org.kde.kwin.Screenshot"

#     def __init__(self, object_path="/Screenshot", bus_name="org.kde.KWin"):
#         super().__init__(object_path=object_path, bus_name=bus_name)
#     def screenshotFullscreen(self, captureCursor):
#         return new_method_call(self, "screenshotFullscreen", "b", (captureCursor,))

#     def screenshotArea(self, x, y, width, height, captureCursor):
#         return new_method_call(
#             self, "screenshotArea", "iiiib", (x, y, width, height, captureCursor)
#         )


log = logging.getLogger(__name__)


class KdeDBusError(Exception):
    pass


class KwinDBusWrapper(CBackend):
    name = "kwin_dbus"
    childprocess = True

    def __init__(self):
        import dbus

        self.dbus = dbus

    def grab(self, bbox=None):
        # bus = self.dbus.SessionBus()
        # proxy = bus.get_object("org.kde.KWin", "/Screenshot")
        # dbus_interface = "org.kde.kwin.Screenshot"

        # https://jeepney.readthedocs.io/en/latest/integrate.html
        connection = connect_and_authenticate(bus="SESSION")
        dbscr = Screenshot()
        if bbox:
            msg = dbscr.screenshotArea(
                bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1], False,
            )
            # buff = proxy.screenshotArea(
            #     bbox[0],
            #     bbox[1],
            #     bbox[2] - bbox[0],
            #     bbox[3] - bbox[1],
            #     dbus_interface=dbus_interface,
            # )
        else:
            # msg = proxy.screenshotFullscreen(False, dbus_interface=dbus_interface)
            msg = dbscr.screenshotFullscreen(False)
        buff = connection.send_and_get_reply(msg)
        print(buff)
        if not buff:
            raise KdeDBusError()

    def backend_version(self):
        return None
