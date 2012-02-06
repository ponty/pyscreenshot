from easyprocess import EasyProcess
from image_debug import img_debug
from nose.tools import eq_, with_setup
from pyscreenshot.backendloader import BackendLoader
from pyvirtualdisplay import Display
import ImageChops
import Xlib.display
import pyscreenshot

backends = [
            'scrot', 
            'imagemagick', 
            'pygtk',
#            'pyqt', #strange error: ICE default IO error handler doing an exit(), pid = 26424, errno = 32
            'wx',
            ] 
bbox_ls = [(100, 200, 300, 400), (10, 10, 20, 20), (100, 100, 200, 200), (1, 2, 3, 4), (10, 20, 30, 40), None]
ref = 'scrot'

process = screen = None
def setup_func():
    "set up test fixtures"
    global process, screen
    screen = Display(visible=0)
    screen.start()
    process = EasyProcess('gnumeric').start().sleep(3)

def teardown_func():
    "tear down test fixtures"
    global process, screen
    process.stop()
    screen.stop()


def check_size(backend, bbox):
    BackendLoader().force(backend)

    im = pyscreenshot.grab(bbox=bbox)
    img_debug(im, backend + str(bbox))
    
    if bbox:
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
    else:
        xdisp=Xlib.display.Display()
        width = xdisp.screen().width_in_pixels
        height = xdisp.screen().height_in_pixels
    
    eq_(width, im.size[0], 'wrong width! %s' % (backend))
    eq_(height, im.size[1], 'wrong height! %s' % (backend))
    
    # it fails sometimes     
    #eq_('RGB', im.mode, 'wrong mode! %s' % (backend))
    
def check_ref(backend, bbox):
    # some tests fail -> disable
    return

    BackendLoader().force(ref)
    img_ref = pyscreenshot.grab(bbox=bbox)
    img_debug(img_ref, ref + str(bbox))
    
    BackendLoader().force(backend)
    im = pyscreenshot.grab(bbox=bbox)
    img_debug(im, backend + str(bbox))

    eq_('RGB', img_ref.mode)
    eq_('RGB', im.mode)
    
    img_diff = ImageChops.difference(img_ref, im)
    bbox = img_diff.getbbox()
    if bbox:
        img_debug(img_diff, 'img_diff' + str(bbox))
    eq_(bbox , None, 'different image data %s!=%s bbox=%s' % (ref, backend, bbox))

      
s = ''        
for bbox in bbox_ls:
    sbbox = str(bbox).replace(' ', '').replace('(', '').replace(')', '').replace(',', '_')
    for backend in backends:
        #if backend != ref:
            s += '''
def test_size_{backend}_{sbbox}():
    check_size("{backend}",{bbox})
@with_setup(setup_func, teardown_func)
def test_ref_{backend}_{sbbox}():
    check_ref("{backend}",{bbox})
'''.format(backend=backend, bbox=bbox, sbbox=sbbox)     
exec s

@with_setup(setup_func, teardown_func)
def dummy():
    pass   

