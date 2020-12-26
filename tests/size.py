import os

from easyprocess import EasyProcess

from pyscreenshot.util import platform_is_linux, platform_is_osx, platform_is_win


def display_size_x():
    # http://www.cyberciti.biz/faq/how-do-i-find-out-screen-resolution-of-my-linux-desktop/
    # xdpyinfo  | grep 'dimensions:'
    screen_width, screen_height = 0, 0
    if not os.environ.get("DISPLAY"):
        raise ValueError("missing DISPLAY variable")
    xdpyinfo = EasyProcess("xdpyinfo")
    xdpyinfo.enable_stdout_log = False
    if xdpyinfo.call().return_code != 0:
        raise ValueError("xdpyinfo error: %s" % xdpyinfo)
    for x in xdpyinfo.stdout.splitlines():
        if "dimensions:" in x:
            screen_width, screen_height = map(int, x.strip().split()[1].split("x"))

    return screen_width, screen_height


def display_size_osx():
    from Quartz import CGDisplayBounds
    from Quartz import CGMainDisplayID

    mainMonitor = CGDisplayBounds(CGMainDisplayID())
    return int(mainMonitor.size.width), int(mainMonitor.size.height)


def display_size_win():
    from win32api import GetSystemMetrics

    return int(GetSystemMetrics(0)), int(GetSystemMetrics(1))


def display_size():
    if platform_is_osx():
        return display_size_osx()

    if platform_is_win():
        return display_size_win()

    if platform_is_linux():
        return display_size_x()
