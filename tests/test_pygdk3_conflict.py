from pyvirtualdisplay import Display
import pyscreenshot
backend = 'pygdk3'


def test_pygdk3_conflict():
    # https://github.com/ponty/pyscreenshot/issues/69
    with Display(visible=0, size=(400, 500)):
        import gi
        gi.require_version('Gdk', '3.0')
        from gi.repository import Gdk
        im = pyscreenshot.grab(backend=backend)
        im = pyscreenshot.grab(backend=backend)  # hangs with multiprocessing


test_pygdk3_conflict.isolate_process = 1
