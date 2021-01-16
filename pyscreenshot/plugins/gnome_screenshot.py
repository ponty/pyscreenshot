from easyprocess import EasyProcess

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import read_prog_img
from pyscreenshot.util import extract_version

PROGRAM = "gnome-screenshot"

# https://gitlab.gnome.org/GNOME/gnome-screenshot/blob/master/src/screenshot-utils.c
# DBus is used for screenshot.
# If it doesn't succeed or $GNOME_SCREENSHOT_FORCE_FALLBACK is set then X DISPLAY is used.
# Flash effect! https://bugzilla.gnome.org/show_bug.cgi?id=672759


class GnomeScreenshotWrapper(CBackend):
    """Plugin for ``pyscreenshot`` that uses ``gnome-screenshot``
    https://git.gnome.org/browse/gnome-screenshot/

    This plugin can take screenshot when system is running Wayland.
    Info: https://bugs.freedesktop.org/show_bug.cgi?id=98672#c1
    """

    name = "gnome-screenshot"
    is_subprocess = True

    def grab(self, bbox=None):
        im = read_prog_img([PROGRAM, "-f"])
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        p = EasyProcess([PROGRAM, "--version"])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()
        return extract_version(p.stdout.replace("-", " "))
