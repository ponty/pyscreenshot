from pyscreenshot.check.speedtest import speedtest
from pyscreenshot.check.versions import print_versions
from pyvirtualdisplay.display import Display
import sys
import os

if sys.platform.startswith('linux'):

 def test_speedtest():
    with Display(visible=0, size=(800, 600)):
        speedtest(virtual_display=True)


def test_print_versions():
    print_versions()

def test_print_versions_no_path():
    path = os.environ["PATH"]
    os.environ["PATH"] = "xxx"
    try:
        print_versions()
    finally:
        os.environ["PATH"] = path
