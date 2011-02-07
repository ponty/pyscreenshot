from pyscreenshot.extract_version import extract_version
from pyscreenshot.proc import Process
from yapsy.IPlugin import IPlugin
import Image
import tempfile

Process().check('import -version', exception=Exception)

class ImagemagickWrapper(IPlugin):
    home_url = 'http://www.imagemagick.org/'
    ubuntu_package = 'imagemagick'
    def __init__(self):
        pass
        #self.is_available = False
        #self.version = None
        
    def activate(self):
        pass
        #self.version = extract_version(p.stdout.replace('-', ' '))
        #self.is_available = (ret == 0)
        
    def grab(self, bbox=None):
        f = tempfile.NamedTemporaryFile(suffix='.png', prefix='screenshot_imagemagick_')
        filename = f.name
        self.grab_to_file(filename, bbox=bbox) 
        im = Image.open(filename)
        #if bbox:
        #    im = im.crop(bbox)
        return im

    def grab_to_file(self, filename, bbox=None):
        command = 'import -window root '  
        if bbox:
            command += " -crop '%sx%s+%s+%s' " % (bbox[2]-bbox[0],bbox[3]-bbox[1], bbox[0], bbox[1])
        command +=filename
        Process(command)
        
    def backend_version(self):
        return extract_version(Process('import -version').stdout.replace('-', ' '))
