from easyprocess import EasyProcess

import pyscreenshot
from config import bbox_ls
from image_debug import img_debug
from pyscreenshot.util import platform_is_linux, platform_is_osx, platform_is_win


def display_size():
    if platform_is_osx():
        from Quartz import CGDisplayBounds
        from Quartz import CGMainDisplayID

        mainMonitor = CGDisplayBounds(CGMainDisplayID())
        return int(mainMonitor.size.width), int(mainMonitor.size.height)

    if platform_is_win():
        from win32api import GetSystemMetrics

        return int(GetSystemMetrics(0)), int(GetSystemMetrics(1))

    if platform_is_linux():
        # http://www.cyberciti.biz/faq/how-do-i-find-out-screen-resolution-of-my-linux-desktop/
        # xdpyinfo  | grep 'dimensions:'
        screen_width, screen_height = 0, 0
        xdpyinfo = EasyProcess("xdpyinfo")
        xdpyinfo.enable_stdout_log = False
        if xdpyinfo.call().return_code != 0:
            raise ValueError("xdpyinfo error: %s" % xdpyinfo)
        for x in xdpyinfo.stdout.splitlines():
            if "dimensions:" in x:
                screen_width, screen_height = map(int, x.strip().split()[1].split("x"))

        return screen_width, screen_height


def check_size(backend, bbox, childprocess=True):
    im = pyscreenshot.grab(bbox=bbox, backend=backend, childprocess=childprocess,)
    img_debug(im, str(backend) + str(bbox))

    if bbox:
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
    else:
        width, height = display_size()
    if width and height:
        assert width == im.size[0]
        assert height == im.size[1]


def backend_size(backend, childprocess=True):
    for bbox in bbox_ls:
        print("bbox: {}".format(bbox))
        print("backend: %s" % backend)
        check_size(backend, bbox, childprocess)
