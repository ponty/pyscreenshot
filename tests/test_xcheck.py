# this test should caome after backend tests
import os

from nose.tools import eq_

from pyscreenshot.util import proc


def test_speedtest():
    eq_(proc("pyscreenshot.check.speedtest").return_code, 0)
    eq_(proc("pyscreenshot.check.speedtest", ["--childprocess", "0"]).return_code, 0)
    eq_(proc("pyscreenshot.check.speedtest", ["--childprocess", "1"]).return_code, 0)


def test_print_versions():
    eq_(proc("pyscreenshot.check.versions").return_code, 0)


def test_print_versions_no_path():
    path = os.environ["PATH"]
    os.environ["PATH"] = "xxx"
    try:
        eq_(proc("pyscreenshot.check.versions").return_code, 0)
    finally:
        os.environ["PATH"] = path


def test_showgrabbox():
    eq_(proc("pyscreenshot.examples.showgrabbox").return_code, 0)


def test_showgrabfullscreen():
    eq_(proc("pyscreenshot.examples.showgrabfullscreen").return_code, 0)
