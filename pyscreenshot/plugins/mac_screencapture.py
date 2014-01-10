import platform
from easyprocess import EasyProcess, EasyProcessCheckInstalledError
from PIL import Image
import tempfile
from ..iplugin import IPlugin

PROGRAM = 'screencapture'
URL = 'http://support.apple.com/kb/ph11229'
PACKAGE = 'screencapture'


class ScreencaptureWrapper(IPlugin):
    name = 'mac_screencapture'
    childprocess = True

    def __init__(self):
        if 'Darwin' not in platform.platform():
            raise EasyProcessCheckInstalledError(self)

    def grab(self, bbox=None):
        f = tempfile.NamedTemporaryFile(
            suffix='.png', prefix='pyscreenshot_screencapture_')
        filename = f.name
        self.grab_to_file(filename, bbox=bbox)
        im = Image.open(filename)
        return im

    def grab_to_file(self, filename, bbox=None):
        command = 'screencapture '
        if bbox:
            command += " -R%s,%s,%s,%s " % (
                bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1])
        command += filename
        EasyProcess(command).call()

    def backend_version(self):
        # TODO:
        return 'not implemented'