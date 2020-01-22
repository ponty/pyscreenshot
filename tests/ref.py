import atexit
import time
import sys

import pyscreenshot
from easyprocess import EasyProcess
from nose.tools import eq_, with_setup
from PIL import ImageChops

from config import bbox_ls
from image_debug import img_debug
from size import backend_size


def check_ref(backend, ref, bbox, childprocess):
    img_ref = pyscreenshot.grab(bbox=bbox, backend=ref, childprocess=childprocess)
    im = pyscreenshot.grab(bbox=bbox, backend=backend, childprocess=childprocess)

    img_ref = img_ref.convert('RGB')
    im = im.convert('RGB')

    eq_('RGB', img_ref.mode)
    eq_('RGB', im.mode)

    img_debug(img_ref, ref + str(bbox))
    img_debug(im, str(backend) + str(bbox))

    img_diff = ImageChops.difference(img_ref, im)
    diff_bbox = img_diff.getbbox()
    if diff_bbox:
        img_debug(img_diff, 'img_diff' + str(diff_bbox))
    eq_(diff_bbox, None, 'different image data %s!=%s bbox=%s diff_bbox=%s' %
        (ref, backend, bbox, diff_bbox))

def backend_ref(backend, ref, childprocess=True):
            for bbox in bbox_ls:
                print('bbox: {}'.format(bbox))
                print('backend: %s' % backend)
                check_ref(backend, ref, bbox, childprocess)

def backend_check(backend, ref=None, childprocess=True):
        if ref is None:
                if sys.platform.startswith('linux'):
                        ref='scrot'
                else:
                        ref='pil'
        if sys.platform != 'darwin':

            backend_ref(backend,
                    ref=ref, 
                    childprocess=childprocess,
                    )
        backend_size(backend, 
                childprocess=childprocess,
                )
