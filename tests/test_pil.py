from bt import backend_to_check
from pyscreenshot.util import platform_is_linux

if not platform_is_linux():

    def test_pil():
        backend_to_check("pil")
