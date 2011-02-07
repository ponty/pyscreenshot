from pyscreenshot.extract_version import extract_version
from pyscreenshot.proc import Process
from yapsy.IPlugin import IPlugin
import Image
import tempfile

Process().check('scrot -version', exception=Exception)

class ScrotWrapper(IPlugin):
    #home_url = 'http://???'
    ubuntu_package = 'scrot'
    
    def __init__(self):
        pass
        
    def activate(self):
        pass
        
    def grab(self, bbox=None):
        f = tempfile.NamedTemporaryFile(suffix='.png', prefix='screenshot_scrot_')
        filename=f.name
        self.grab_to_file(filename) 
        im = Image.open(filename)
        if bbox:
            im = im.crop(bbox)
        return im

    def grab_to_file(self, filename):
        Process('scrot ' + filename)

    def backend_version(self):
        return extract_version(Process('scrot -version').stdout)
        
