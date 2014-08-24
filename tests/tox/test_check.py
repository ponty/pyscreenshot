from pyscreenshot.check import virtualtest
from pyscreenshot.check.speedtest import speedtest
from pyscreenshot.check.versions import print_versions


def test_speedtest():
    speedtest()


def test_print_versions():
    print_versions()


def test_virtualtest():
    virtualtest.main()
