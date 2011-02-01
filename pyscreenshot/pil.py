from pyscreenshot import utils
from pyscreenshot.proc import Process
from yapsy.IPlugin import IPlugin
import Image
import ImageGrab

class PilWrapper(IPlugin):
    '''windows only'''
    
    home_url = 'http://www.pythonware.com/products/pil/'
    ubuntu_package = 'python-imaging'
    def __init__(self):
        self.is_available = True
        self.version = Image.VERSION
        
    def activate(self):
        pass
        
    def grab(self, bbox=None):
        return ImageGrab.grab(bbox)
        
    def grab_to_file(self, filename):
        im=self.grab()
        im.save(filename)
