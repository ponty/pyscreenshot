from logging import DEBUG
from tempfile import mkdtemp, gettempdir
import logging
import os

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
        root = gettempdir() + '/img_debug'
        if not os.path.exists(root):
            os.makedirs(root, mode=0777)
        img_dir = mkdtemp(prefix='img_debug_', suffix='', dir=root)
    if CROP_RECT:
        im = im.crop(CROP_RECT)
    fname = img_dir + '/' + str(img_ind) + '_' + text + '.png'
    im.save(fname)
    log.debug('image (%s) was saved:' % im + fname)
    img_ind += 1
# BackendLoader().selected().name + '_'
