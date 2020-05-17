from bt import backend_to_check, check_import
from pyscreenshot.util import platform_is_osx

if not platform_is_osx() and check_import("wx"):

    def test_wx():
        backend_to_check("wx")
