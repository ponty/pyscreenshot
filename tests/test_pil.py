from bt import backend_to_check

from pyscreenshot.util import (
    platform_is_linux,
    platform_is_osx,
    platform_is_win,
    use_x_display,
)

ok = False
if platform_is_osx() and not use_x_display():
    ok = True
if platform_is_linux() and use_x_display():
    ok = True
if platform_is_win():
    ok = True

if ok:

    def test_pil():
        backend_to_check("pil")
