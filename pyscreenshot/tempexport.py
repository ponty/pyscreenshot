import os.path

from easyprocess import EasyProcess
from PIL import Image

from pyscreenshot.tempdir import TemporaryDirectory


class RunProgError(Exception):
    pass


def read_func_img(func, bbox=None):
    with TemporaryDirectory(prefix="pyscreenshot") as tmpdirname:
        filename = os.path.join(tmpdirname, "screenshot.png")
        func(filename, bbox)
        im = Image.open(filename)
        return im


def read_prog_img(cmd):
    def run_prog(filename, bbox=None):
        p = EasyProcess(cmd + [filename])
        p.call()
        if p.return_code != 0:
            raise RunProgError(p.stderr)

    im = read_func_img(run_prog)
    return im


def extract_version(txt):
    """This function tries to extract the version from the help text of any
    program."""
    words = txt.replace(",", " ").split()
    version = None
    for x in reversed(words):
        if len(x) > 2:
            if x[0].lower() == "v":
                x = x[1:]
            if "." in x and x[0].isdigit():
                version = x
                break
    return version
