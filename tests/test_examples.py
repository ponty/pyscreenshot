import os
from tempfile import TemporaryDirectory

from bt import prog_check
from pyscreenshot.util import run_mod_as_subproc


def check_example(name):
    owd = os.getcwd()
    with TemporaryDirectory(prefix="pyscreenshot") as tmpdirname:
        try:
            os.chdir(tmpdirname)
            assert run_mod_as_subproc("pyscreenshot.examples." + name).return_code == 0
        finally:
            os.chdir(owd)


def test_grabbox():
    check_example("grabbox")


def test_grabfullscreen():
    check_example("grabfullscreen")


if prog_check(["Xvfb", "-version"]):

    def test_virtdisp():
        check_example("virtdisp")
