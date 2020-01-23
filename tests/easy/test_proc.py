from nose.tools import eq_, raises

from pyscreenshot.procutil import run_in_childprocess

# win error with lambda: Can't pickle local object '...<lambda>'


def f3():
    return 3


def f3px(x):
    return 3 + x


def f4px(x):
    return 4 + x


def test():
    eq_(3, run_in_childprocess(f3))
    eq_(4, run_in_childprocess(f3px, None, 1))
    eq_(5, run_in_childprocess(f3px, None, x=2))


def test_codec():
    coder = decoder = f4px
    eq_(12, run_in_childprocess(f3px, (coder, decoder), 1))


def exc():
    raise ValueError("error!")


@raises(ValueError)
def test_exc():
    eq_(3, run_in_childprocess(exc))
