from easyprocess import EasyProcess
from PIL import Image
from pyscreenshot.tempexport import read_prog_img, extract_version

PROGRAM = 'import'
# http://www.imagemagick.org/


class ImagemagickWrapper(object):
    name = 'imagemagick'
    childprocess = True

    def __init__(self):
        p = EasyProcess([PROGRAM, '-version'])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()

    def grab(self, bbox=None):
        command = [PROGRAM, '-silent', '-window', 'root']
        if bbox:
            pbox = '{}x{}+{}+{}'.format(
                bbox[2] - bbox[0], bbox[3] - bbox[1], bbox[0], bbox[1])
            command += ['-crop', pbox]
        im = read_prog_img(command)
        return im

    def backend_version(self):
        return extract_version(
            EasyProcess([PROGRAM, '-version']).call().stdout.replace('-', ' '))
