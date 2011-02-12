from logging import DEBUG
from path import path
from pyscreenshot.backendloader import BackendLoader
from tempfile import mkdtemp, gettempdir
import logging

log = logging.getLogger(__name__)

img_dir = None
img_ind = 0
CROP_RECT = None

def set_crop_rect(rct):
    global CROP_RECT
    CROP_RECT = rct
    
def img_debug(im, text):
    if not log.isEnabledFor(DEBUG):
        return
    global img_dir
    global img_ind
    if not img_dir:
        root = path(gettempdir()) / 'img_debug'
        if not root.exists():
            root.makedirs()
        img_dir = path(mkdtemp(prefix='img_debug_', suffix='', dir=root))
    if CROP_RECT:
        im = im.crop(CROP_RECT)
    fname = str(img_dir /  str(img_ind) + '_' + text + '.png')
    im.save(fname)
    log.debug('image (%s) was saved:' % im + fname)
    img_ind += 1
#BackendLoader().selected().name + '_'
