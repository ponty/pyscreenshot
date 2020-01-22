from nose.tools import eq_

from pyscreenshot.procutil import proc


def test_showgrabbox():
   eq_(proc('pyscreenshot.examples.showgrabbox').return_code,0)


def test_showgrabfullscreen():
   eq_(proc('pyscreenshot.examples.showgrabfullscreen').return_code,0)
