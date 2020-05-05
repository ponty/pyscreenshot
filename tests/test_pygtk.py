from pyscreenshot.util import py2
from ref import backend_to_check, check_import

# no pygtk for py3
if py2() and check_import("gtk"):

    def test_pygtk():
        backend_to_check("pygtk")
