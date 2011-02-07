from pyscreenshot.extract_version import extract_version
from pyscreenshot.proc import Process
from yapsy.IPlugin import IPlugin
import Image
import tempfile
from gtk.gdk import Pixbuf, COLORSPACE_RGB, get_default_root_window


class GtkPixbufWrapper(IPlugin):
    #home_url = 'http://???'
    ubuntu_package = 'scrot'
    def __init__(self):
        self.is_available = False
        self.version = None
        
    def activate(self):
        p = Process()
        ret=p.call('scrot -version')
        self.version = extract_version(p.stdout)
        self.is_available = (ret==0)
        
    def grab(self, bbox=None):
        f = tempfile.NamedTemporaryFile(suffix='.png', prefix='screenshot_gtkpixbuf_')
        filename=f.name
        self.grab_to_file(filename) 
        im = Image.open(filename)
        if bbox:
            im = im.crop(bbox)
        return im

    def grab_to_file(self, filename):
        '''
        based on: http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux
        
        http://www.pygtk.org/docs/pygtk/class-gdkpixbuf.html
        
        only "jpeg" or "png"
        '''
        w = get_default_root_window()
        sz = w.get_size()
        #print "The size of the window is %d x %d" % sz
        pb = Pixbuf(COLORSPACE_RGB,False,8,sz[0],sz[1])
        pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
        assert pb
        type="png"
        if filename.endswith('.jpeg'):
            type="jpeg"
            
        pb.save(filename,type)
        
    def backend_version(self):
        # TODO:
        return 'unknown'
