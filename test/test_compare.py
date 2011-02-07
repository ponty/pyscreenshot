from Xlib.display import Display
from image_debug import img_debug
from nose.tools import eq_
import ImageChops
import pyscreenshot

backends = ['scrot', 'imagemagick', 'pygtk'] 
bbox_ls = [(100,200,300,400),(10, 10, 20, 20), (100, 100, 200, 200), (1, 2, 3, 4), (10, 20, 30, 40), None]
ref = 'scrot'



def check_size(backend, bbox):
    im = pyscreenshot.grab(bbox=bbox, force_backend=backend)
    img_debug(im, backend+str(bbox))
    
    if bbox:
        width=bbox[2]-bbox[0]
        height=bbox[3]-bbox[1]
    else:
        width = Display().screen().width_in_pixels
        height = Display().screen().height_in_pixels
        
    eq_(width, im.size[0], 'wrong width! %s' % (backend))
    eq_(height, im.size[1], 'wrong height! %s' % (backend))
    
def check_ref(backend, bbox):
    img_ref = pyscreenshot.grab(bbox=bbox, force_backend=ref)
    img_debug(img_ref, ref+str(bbox))
    
    im = pyscreenshot.grab(bbox=bbox, force_backend=backend)
    img_debug(im, backend+str(bbox))
    
    img_diff = ImageChops.difference(img_ref, im)
    bbox = img_diff.getbbox()
    if bbox:
        img_debug(img_diff, 'img_diff'+str(bbox))
    assert bbox is None, 'different image data %s!=%s bbox=%s' % (ref, backend, bbox)

      
s = ''        
for bbox in bbox_ls:
    sbbox = str(bbox).replace(' ', '').replace('(', '').replace(')', '').replace(',', '_')
    for backend in backends:
        #if backend != ref:
            s += '''
def test_size_{backend}_{sbbox}():
    check_size("{backend}",{bbox})
def test_ref_{backend}_{sbbox}():
    check_ref("{backend}",{bbox})
'''.format(backend=backend, bbox=bbox, sbbox=sbbox)     
exec s

