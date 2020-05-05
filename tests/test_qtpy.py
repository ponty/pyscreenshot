from pyscreenshot.util import platform_is_osx
from ref import backend_to_check, check_import

# qt color problem on osx
if not platform_is_osx():

    if check_import("qtpy"):

        def test_qtpy():
            backend_to_check("qtpy")
