from bt import backend_to_check, check_import
from pyscreenshot.util import use_x_display

ok = False
if check_import("gi"):
    if use_x_display():
        import gi

        # Arch: AttributeError: module 'gi' has no attribute 'require_version'
        try:
            gi.require_version("Gdk", "3.0")
            ok = True
        except AttributeError:
            pass
        except ValueError:
            pass
if ok:

    def test_pygdk3():
        backend_to_check("pygdk3")
