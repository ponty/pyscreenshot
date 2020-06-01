# this test should come after backend tests
import os

from pyscreenshot.util import run_mod_as_subproc


def test_speedtest():
    assert run_mod_as_subproc("pyscreenshot.check.speedtest").return_code == 0
    assert (
        run_mod_as_subproc(
            "pyscreenshot.check.speedtest", ["--childprocess", "0"]
        ).return_code
        == 0
    )
    assert (
        run_mod_as_subproc(
            "pyscreenshot.check.speedtest", ["--childprocess", "1"]
        ).return_code
        == 0
    )


def test_print_versions():
    assert run_mod_as_subproc("pyscreenshot.check.versions").return_code == 0


def test_print_versions_no_path():
    path = os.environ["PATH"]
    os.environ["PATH"] = "xxx"
    try:
        assert run_mod_as_subproc("pyscreenshot.check.versions").return_code == 0
    finally:
        os.environ["PATH"] = path
