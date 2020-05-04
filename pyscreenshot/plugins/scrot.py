import logging

from easyprocess import EasyProcess
from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import read_prog_img
from pyscreenshot.util import extract_version

log = logging.getLogger(__name__)


PROGRAM = "scrot"


class ScrotWrapper(CBackend):
    name = "scrot"
    childprocess = True

    def __init__(self):
        pass

    def grab(self, bbox=None):
        # p = EasyProcess([PROGRAM, "-version"])
        # p.enable_stdout_log = False
        # p.enable_stderr_log = False
        # p.call()

        im = read_prog_img([PROGRAM, "--silent"])
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return extract_version(EasyProcess([PROGRAM, "-version"]).call().stdout)
