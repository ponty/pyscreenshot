from easyprocess import EasyProcess
from easyprocess import extract_version
from PIL import Image
import tempfile

PROGRAM = 'gnome-screenshot'


class GnomeScreenshotBackendError(Exception):
    pass


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
        self._grab_to_file(filename)
        im = Image.open(filename)
        if bbox:
            im = im.crop(bbox)
        return im

    def _grab_to_file(self, filename):
        command = [PROGRAM, '-f', filename]
        p = EasyProcess(command)
        p.call()
        if p.return_code != 0:
            raise GnomeScreenshotBackendError(p.stderr)

    def backend_version(self):
        return extract_version(
            EasyProcess([PROGRAM, '--version']).call().stdout.replace('-', ' '))
