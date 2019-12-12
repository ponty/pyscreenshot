from pyscreenshot.tempdir import TemporaryDirectory
import os.path
from easyprocess import EasyProcess
from PIL import Image


def read_func_img(func, bbox=None):
    with TemporaryDirectory(prefix='pyscreenshot') as tmpdirname:
        filename = os.path.join(tmpdirname, 'screenshot.png')
        func(filename, bbox)
        im = Image.open(filename)
        return im


def read_prog_img(cmd):
    def run_prog(filename, bbox=None):
        p = EasyProcess(cmd+[filename])
        p.call()
    im = read_func_img(run_prog)
    return im
