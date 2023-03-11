import logging
import os

from easyprocess import EasyProcess
from PIL import Image

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import RunProgError

log = logging.getLogger(__name__)


PROGRAM = "ksnip"


class KsnipWrapper(CBackend):
    name = "ksnip"
    is_subprocess = True

    def grab(self, bbox=None):
        cmd = [PROGRAM, "--fullscreen", "--save"]
        p = EasyProcess(cmd)
        p.call()
        if p.return_code != 0:
            raise RunProgError(p.stderr)
        lastline = p.stdout.splitlines()[-1]
        if "Image Saved" not in lastline:
            raise RunProgError(p.stderr)
        filename = lastline.split()[-1]
        im = Image.open(filename)
        os.remove(filename)

        # TODO: bbox param
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        for line in EasyProcess([PROGRAM, "--version"]).call().stderr.splitlines():
            if "version" in line.lower():
                return line.split()[-1]
