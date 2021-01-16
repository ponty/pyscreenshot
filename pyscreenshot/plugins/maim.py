import logging

from easyprocess import EasyProcess

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import read_prog_img
from pyscreenshot.util import extract_version

log = logging.getLogger(__name__)


PROGRAM = "maim"


class MaimWrapper(CBackend):
    name = "maim"
    is_subprocess = True

    def grab(self, bbox=None):
        cmd = [PROGRAM, "--hidecursor"]
        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            # https://github.com/naelstrof/maim/issues/119
            cmd += ["-g", "{}x{}+{}+{}".format(width, height, bbox[0], bbox[1])]
        im = read_prog_img(cmd)
        return im

    def backend_version(self):
        return extract_version(EasyProcess([PROGRAM, "--version"]).call().stdout)
