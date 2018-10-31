from nose.tools import eq_, raises

from pyscreenshot.procutil import run_in_childprocess


def test():
    eq_(3, run_in_childprocess(lambda : 3))
    eq_(4, run_in_childprocess(lambda x: 3+x,None, 1))
    eq_(5, run_in_childprocess(lambda x: 3+x,None, x=2))
    
def test_codec():
    coder= decoder=lambda x:x+4
    eq_(12, run_in_childprocess(lambda x: 3+x,(coder, decoder), 1))
    
def exc():
    raise ValueError('error!')
    
@raises(ValueError)
def test_exc():
    eq_(3, run_in_childprocess(exc))
