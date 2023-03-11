import logging
import os

from PIL import Image

from pyscreenshot.plugins.backend import UNKNOWN_VERSION, CBackend

log = logging.getLogger(__name__)


class FreedesktopDBusError(Exception):
    pass


class FreedesktopDBusWrapper(CBackend):
    name = "freedesktop_dbus"
    is_subprocess = True

    def grab(self, bbox=None):
        has_jeepney = False
        try:
            from jeepney import DBusAddress, new_method_call
            from jeepney.bus_messages import MatchRule, message_bus
            from jeepney.io.blocking import Proxy, open_dbus_connection

            has_jeepney = True
        except ImportError:
            pass

        if not has_jeepney:
            raise FreedesktopDBusError("jeepney library is missing")

        portal = DBusAddress(
            object_path="/org/freedesktop/portal/desktop",
            bus_name="org.freedesktop.portal.Desktop",
        )
        screenshot = portal.with_interface("org.freedesktop.portal.Screenshot")

        conn = open_dbus_connection()

        token = "pyscreenshot"
        sender_name = conn.unique_name[1:].replace(".", "_")
        handle = f"/org/freedesktop/portal/desktop/request/{sender_name}/{token}"

        response_rule = MatchRule(
            type="signal", interface="org.freedesktop.portal.Request", path=handle
        )
        Proxy(message_bus, conn).AddMatch(response_rule)

        with conn.filter(response_rule) as responses:
            req = new_method_call(
                screenshot,
                "Screenshot",
                "sa{sv}",
                ("", {"handle_token": ("s", token), "interactive": ("b", False)}),
            )
            conn.send_and_get_reply(req)
            response_msg = conn.recv_until_filtered(responses)

        response, results = response_msg.body

        im = False
        if response == 0:
            filename = results["uri"][1].split("file://", 1)[-1]
            if os.path.isfile(filename):
                im = Image.open(filename)
                os.remove(filename)

        conn.close()

        if bbox and im:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return UNKNOWN_VERSION
