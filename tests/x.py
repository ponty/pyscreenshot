from Xlib import X, display, Xutil
from Xlib.ext import randr
import sys

LINUX = sys.platform.startswith("linux")

# https://github.com/python-xlib/python-xlib/blob/master/examples/xrandr.py#L44
def missing_RANDR():
    if not LINUX:
        return False
    disp = display.Display()
    return not disp.has_extension("RANDR")
