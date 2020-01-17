from easyprocess import EasyProcess
from image_debug import img_debug
from nose.tools import eq_
from nose.tools import with_setup
from pyvirtualdisplay import Display
from PIL import ImageChops
import sys
import pyscreenshot
from config import bbox_ls


def display_size():
    if sys.platform == "darwin":
        from Quartz import CGDisplayBounds
        from Quartz import CGMainDisplayID

        mainMonitor = CGDisplayBounds(CGMainDisplayID())
        return (mainMonitor.size.width, mainMonitor.size.height) 

    # http://www.cyberciti.biz/faq/how-do-i-find-out-screen-resolution-of-my-linux-desktop/
    # xdpyinfo  | grep 'dimensions:'
    screen_width, screen_height = None, None
    xdpyinfo = EasyProcess('xdpyinfo')
    xdpyinfo.enable_stdout_log = False
    for x in xdpyinfo.call().stdout.splitlines():
        if 'dimensions:' in x:
            screen_width, screen_height = map(int, x.strip().split()[1].split('x'))

    return screen_width, screen_height


def check_size(backend, bbox, childprocess=True):
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
        if width and height:
            eq_(width, im.size[0])
            eq_(height, im.size[1])


def _backend_size(backend, childprocess=True):
    for bbox in bbox_ls:
        print('bbox: {}'.format(bbox))
        print('backend: %s' % backend)
        check_size(backend, bbox, childprocess)


def backend_size(backend, virtual_display=True, childprocess=True):
    if virtual_display:
        with Display(visible=0, size=(800, 600)):
            _backend_size(backend, childprocess)
    else:
        _backend_size(backend, childprocess)
