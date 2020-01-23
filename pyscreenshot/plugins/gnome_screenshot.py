from easyprocess import EasyProcess

from pyscreenshot.tempexport import extract_version, read_prog_img

PROGRAM = "gnome-screenshot"


class GnomeScreenshotWrapper(object):

    """Plugin for ``pyscreenshot`` that uses ``gnome-screenshot``
    https://git.gnome.org/browse/gnome-screenshot/

    This plugin can take screenshot when system is running Wayland.
    Info: https://bugs.freedesktop.org/show_bug.cgi?id=98672#c1
    """

    name = "gnome-screenshot"
    childprocess = True

    def __init__(self):
        p = EasyProcess([PROGRAM, "--version"])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()

    def grab(self, bbox=None):
        im = read_prog_img([PROGRAM, "-f"])
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return extract_version(
            EasyProcess([PROGRAM, "--version"]).call().stdout.replace("-", " ")
        )
