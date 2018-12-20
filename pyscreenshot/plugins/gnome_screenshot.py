from easyprocess import EasyProcess
from easyprocess import extract_version
from PIL import Image
import tempfile

PROGRAM = 'gnome-screenshot'


class GnomeScreenshotWrapper(object):

    """Plugin for ``pyscreenshot`` that uses ``gnome-screenshot``
    https://git.gnome.org/browse/gnome-screenshot/

    This plugin can take screenshot when system is running Wayland.
    Info: https://bugs.freedesktop.org/show_bug.cgi?id=98672#c1
    """
    name = 'gnome-screenshot'
    childprocess = True

    def __init__(self):
        EasyProcess([PROGRAM, '--version']).check_installed()

    def grab(self, bbox=None):
        f = tempfile.NamedTemporaryFile(
            suffix='.png', prefix='pyscreenshot_gnome_screenshot_')
        filename = f.name
        self.grab_to_file(filename, bbox=bbox)
        im = Image.open(filename)
        return im

    def grab_to_file(self, filename, bbox=None):
        if bbox:
            f = tempfile.NamedTemporaryFile(
                suffix='.png', prefix='pyscreenshot_gnome_screenshot_tmp_')
            tmp_filename = f.name
        else:
            tmp_filename = filename

        command = [PROGRAM, '-f', tmp_filename]
        EasyProcess(command).call()

        if bbox:
            im = Image.open(tmp_filename)
            new_im = im.crop(bbox)
            new_im.save(filename)

    def backend_version(self):
        return extract_version(
            EasyProcess([PROGRAM, '--version']).call().stdout.replace('-', ' '))
