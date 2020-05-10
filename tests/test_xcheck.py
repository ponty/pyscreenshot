# this test should come after backend tests
import os

from pyscreenshot.util import proc


def test_speedtest():
    assert proc("pyscreenshot.check.speedtest").return_code == 0
    assert (
        proc("pyscreenshot.check.speedtest", ["--childprocess", "0"]).return_code == 0
    )
    assert (
        proc("pyscreenshot.check.speedtest", ["--childprocess", "1"]).return_code == 0
    )


def test_print_versions():
    assert proc("pyscreenshot.check.versions").return_code == 0


def test_print_versions_no_path():
    path = os.environ["PATH"]
    os.environ["PATH"] = "xxx"
    try:
        assert proc("pyscreenshot.check.versions").return_code == 0
    finally:
        os.environ["PATH"] = path


# def test_showgrabbox():
#     assert proc("pyscreenshot.examples.showgrabbox").return_code == 0


# def test_showgrabfullscreen():
#     assert proc("pyscreenshot.examples.showgrabfullscreen").return_code == 0
