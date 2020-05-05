from pyscreenshot.util import platform_is_linux
from ref import backend_to_check

if not platform_is_linux():

    def test_pil():
        backend_to_check("pil")
