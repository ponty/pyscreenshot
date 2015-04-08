from pyscreenshot.check.speedtest import speedtest
from pyscreenshot.check.versions import print_versions
from pyvirtualdisplay.display import Display


def test_speedtest():
    with Display(visible=0, size=(800, 600)):
        speedtest()


def test_print_versions():
    print_versions()

