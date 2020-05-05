from pyscreenshot.util import use_x_display
from ref import backend_to_check, check_import

ok = False
if check_import("gi"):
    if use_x_display():
        import gi

        # Arch: AttributeError: module 'gi' has no attribute 'require_version'
        try:
            gi.require_version
            ok = True
        except AttributeError:
            pass
if ok:

    def test_pygdk3():
        backend_to_check("pygdk3")
