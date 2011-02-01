from pyscreenshot import utils
from pyscreenshot.proc import Process
from yapsy.IPlugin import IPlugin
import Image
import tempfile

class ImagemagickWrapper(IPlugin):
    #home_url = 'http://'
    ubuntu_package = 'imagemagick'
    def __init__(self):
        self.is_available = False
        self.version = None
        
    def activate(self):
        p = Process()
        p.call('import -version')
        self.version = utils.extract_version(p.stdout)
        self.is_available = self.version
        
    def grab(self, bbox=None):
        f = tempfile.NamedTemporaryFile(suffix='.png', prefix='screenshot_imagemagick_')
        filename=f.name
        self.grab_to_file(filename) 
        im = Image.open(filename)
        if bbox:
            im = im.crop(bbox)
        return im

    def grab_to_file(self, filename):
        command = 'import -window root ' + filename 
        p = Process()
        p.call(command)
        
