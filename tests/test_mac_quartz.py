from pyscreenshot.util import platform_is_osx
from ref import backend_to_check

if platform_is_osx():

    def test_mac_quartz():
        backend_to_check("mac_quartz")
