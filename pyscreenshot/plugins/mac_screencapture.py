from easyprocess import EasyProcess

from pyscreenshot.plugins.backend import UNKNOWN_VERSION, CBackend
from pyscreenshot.tempexport import read_prog_img
from pyscreenshot.util import platform_is_osx

PROGRAM = "screencapture"
# https://ss64.com/osx/screencapture.html
#  By default screneshots are saved as .png files,


class ScreencaptureError(Exception):
    pass


class ScreencaptureWrapper(CBackend):
    name = "mac_screencapture"
    is_subprocess = True

    def grab(self, bbox=None):
        if not platform_is_osx():
            raise ScreencaptureError("This backend runs only on Darwin")

        command = [PROGRAM, "-x"]
        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            command += ["-R{},{},{},{}".format(bbox[0], bbox[1], width, height)]
        im = read_prog_img(command)
        return im

    def backend_version(self):
        p = EasyProcess([PROGRAM, "-help"])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()
        if p.return_code == 0:
            return UNKNOWN_VERSION
