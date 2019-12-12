from easyprocess import EasyProcess
from easyprocess import extract_version
from PIL import Image
import logging
from pyscreenshot.tempexport import read_prog_img

log = logging.getLogger(__name__)


PROGRAM = 'scrot'


class ScrotWrapper(object):
    name = 'scrot'
    childprocess = True

    def __init__(self):
        EasyProcess([PROGRAM, '-version']).check_installed()

    def grab(self, bbox=None):
        im = read_prog_img([PROGRAM, '--silent'])
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return extract_version(
            EasyProcess([PROGRAM, '-version']).call().stdout)
