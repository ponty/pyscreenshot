import platform

from easyprocess import EasyProcess

from pyscreenshot.tempexport import read_prog_img

PROGRAM = "screencapture"
# https://ss64.com/osx/screencapture.html
#  By default screneshots are saved as .png files,


class ScreencaptureWrapper(object):
    name = "mac_screencapture"
    childprocess = True

    def __init__(self):
        if "Darwin" not in platform.platform():
            raise RunProgError("This backend runs only on Darwin")
        p = EasyProcess([PROGRAM, "-help"])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()

    def grab(self, bbox=None):
        command = [PROGRAM, "-x"]
        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            command += ["-R{},{},{},{}".format(bbox[0], bbox[1], width, height)]
        im = read_prog_img(command)
        return im

    def backend_version(self):
        # TODO:
        return "X.X"
