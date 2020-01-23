import sys

from easyprocess import EasyProcess

from pyscreenshot.tempexport import extract_version, read_prog_img

PROGRAM = "import"
# http://www.imagemagick.org/


class ImagemagickBackendError(Exception):
    pass


class ImagemagickWrapper(object):
    name = "imagemagick"
    childprocess = True

    def __init__(self):
        if sys.platform == "darwin":
            raise ImagemagickBackendError("osx not supported")  # TODO

        p = EasyProcess([PROGRAM, "-version"])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()

    def grab(self, bbox=None):
        command = [PROGRAM, "-silent", "-window", "root"]
        if bbox:
            pbox = "{}x{}+{}+{}".format(
                bbox[2] - bbox[0], bbox[3] - bbox[1], bbox[0], bbox[1]
            )
            command += ["-crop", pbox]
        im = read_prog_img(command)
        return im

    def backend_version(self):
        stdout = EasyProcess([PROGRAM, "-version"]).call().stdout
        s = stdout.splitlines()[0]
        return extract_version(s.replace("-", " "))
