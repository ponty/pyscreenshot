import six
from nose.tools import assert_raises
from pyscreenshot import FailedBackendError
from pyscreenshot.util import (
    platform_is_linux,
    platform_is_osx,
    platform_is_win,
    use_x_display,
)

import x
from ref import backend_to_check, check_import

ok = False
if not six.PY2 and check_import("mss"):
    if platform_is_osx() and not use_x_display():
        ok = True
    if platform_is_linux() and use_x_display():
        ok = True
    if platform_is_win():
        ok = True

if ok:

    def test_mss():
        if x.missing_RANDR():
            try:
                backend_to_check("mss")
            except FailedBackendError:
                pass
        else:
            backend_to_check("mss")
