from pyscreenshot.util import platform_is_osx, py2
from bt import backend_to_check, check_import

# qt color problem on osx
if not platform_is_osx():

    if not py2() and check_import("PySide2"):

        def test_pyside2():
            backend_to_check("pyside2")
