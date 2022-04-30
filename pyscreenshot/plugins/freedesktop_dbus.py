import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from PIL import Image
import os
import shutil
import tempfile

from pyscreenshot.plugins.backend import UNKNOWN_VERSION, CBackend


DBusGMainLoop(set_as_default=True)
loop = GLib.MainLoop()
bus = dbus.SessionBus()

# A better reference could be to implement this:
# https://gist.github.com/danshick/3446dac24c64ce6172eced4ac255ac3d
# This file has a very simple implementation.
# It uses org.freedesktop.portal.Screenshot DBus interface,
# so it asks for user permission to share the screenshot


class FreedesktopDBusWrapper(CBackend):
    """Plugin for ``pyscreenshot`` that uses Freedesktop's
    org.freedesktop.portal.Screenshot DBus interface

    This plugin can take screenshot when system is running Wayland.
    """

    name = "freedesktop-portal"
    is_subprocess = True

    def backend_version(self):
        return UNKNOWN_VERSION

    def grab(self, bbox=None):
        tempdir = tempfile.TemporaryDirectory()
        img_tmp_path = os.path.join(tempdir.name, 'screenshot.png')

        im = False

        def handler(*args, **kwargs):
            if args[0] == 0:
                shutil.move(str(args[1]['uri']).split('file://', 1)[-1], img_tmp_path)
            loop.quit()

        bus.add_signal_receiver(handler, signal_name='Response', dbus_interface='org.freedesktop.portal.Request')
        proxy = bus.get_object('org.freedesktop.portal.Desktop', '/org/freedesktop/portal/desktop')
        screenshot_iface = dbus.Interface(proxy, dbus_interface='org.freedesktop.portal.Screenshot')
        screenshot_iface.Screenshot('', {'interactive': False})

        loop.run()

        if os.path.isfile(img_tmp_path):
            im = Image.open(img_tmp_path)

        if bbox and im:
            im = im.crop(bbox)

        return im
