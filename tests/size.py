from easyprocess import EasyProcess
from image_debug import img_debug
from nose.tools import eq_
from nose.tools import with_setup
from pyvirtualdisplay import Display
from PIL import ImageChops
import pyscreenshot
from config import bbox_ls


def display_size():
    # http://www.cyberciti.biz/faq/how-do-i-find-out-screen-resolution-of-my-linux-desktop/
    # xdpyinfo  | grep 'dimensions:'
    for x in EasyProcess('xdpyinfo').call().stdout.splitlines():
        if 'dimensions:' in x:
            screen_width, screen_height = map(
                int, x.strip().split()[1].split('x'))

    return screen_width, screen_height


def check_size(backend, bbox):
    for childprocess in [True]:
        im = pyscreenshot.grab(
            bbox=bbox,
            backend=backend,
            childprocess=childprocess,
        )
        img_debug(im, backend + str(bbox))

        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
        else:
            width, height = display_size()

        eq_(width, im.size[0])
        eq_(height, im.size[1])


def backend_size(backend):
    with Display(visible=0, size=(800, 600)):
        for bbox in bbox_ls:
            print('bbox: {}'.format(bbox))
            print('backend: %s' % backend)
            check_size(backend, bbox)
