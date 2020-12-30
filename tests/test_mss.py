from bt import backend_to_check, check_import
from pyscreenshot import FailedBackendError
from pyscreenshot.util import (
    platform_is_linux,
    platform_is_osx,
    platform_is_win,
    use_x_display,
)

try:
    from Xlib import display
except ImportError:
    display = None

# https://github.com/python-xlib/python-xlib/blob/master/examples/xrandr.py#L44
def missing_RANDR():
    if platform_is_osx():
        return False
    if not display:
        return False
    disp = display.Display()
    return not disp.has_extension("RANDR")


ok = False
if check_import("mss"):
    if platform_is_osx() and not use_x_display():
        ok = True
    if platform_is_linux() and use_x_display():
        ok = True
    if platform_is_win():
        ok = True

if ok:

    def test_mss():
        if missing_RANDR():
            try:
                backend_to_check("mss")
            except FailedBackendError:
                pass
        else:
            backend_to_check("mss")
