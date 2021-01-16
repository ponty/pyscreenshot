"""
Backend for grim (https://github.com/emersion/grim), a Wayland screen tool for
environments other than Gnome and KDE, such as Sway.
"""
import logging

from easyprocess import EasyProcess

from pyscreenshot.plugins.backend import UNKNOWN_VERSION, CBackend
from pyscreenshot.tempexport import read_prog_img

log = logging.getLogger(__name__)


PROGRAM = "grim"


class GrimWrapper(CBackend):
    name = "grim"
    is_subprocess = True

    def _bbox_to_grim_region(self, bbox):
        """
        Translate pyscreenshot's bbox tuple convention of (x1, y1, x2, y2) to
        grim's bbox convention, which is a string of the following format:
        <x>,<y> <width>x<height>
        """
        x1, y1, x2, y2 = bbox
        width = x2 - x1
        height = y2 - y1
        return "{},{} {}x{}".format(x1, y1, width, height)

    def grab(self, bbox=None):
        if bbox:
            # using grim's built-in cropping feature
            region = self._bbox_to_grim_region(bbox)
            return read_prog_img([PROGRAM, "-g", region])
        return read_prog_img([PROGRAM])

    def backend_version(self):
        # grim doesn't have a version flag for some reason
        p = EasyProcess([PROGRAM, "-help"])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()
        if p.return_code == 0:
            return UNKNOWN_VERSION
