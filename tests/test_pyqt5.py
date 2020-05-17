from bt import backend_to_check, check_import
from pyscreenshot.util import platform_is_osx

# qt color problem on osx
if not platform_is_osx():

    if check_import("PyQt5"):

        def test_pyqt5():
            backend_to_check("pyqt5")
