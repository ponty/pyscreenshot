from ref import backend_check


def test_default():
    backend_check(None, childprocess=True)
    backend_check(None, childprocess=False)
