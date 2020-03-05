import sys

from pyscreenshot.util import platform_is_linux
from Xlib import X, Xutil, display
from Xlib.ext import randr


# https://github.com/python-xlib/python-xlib/blob/master/examples/xrandr.py#L44
def missing_RANDR():
    if not platform_is_linux():
        return False
    disp = display.Display()
    return not disp.has_extension("RANDR")


# TODO: move x.py to mss
