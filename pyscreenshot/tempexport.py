import os.path
from tempfile import TemporaryDirectory

from easyprocess import EasyProcess
from PIL import Image


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
