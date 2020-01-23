from ref import backend_check


def test_wx():
    backend_check("wx", childprocess=True)
    backend_check("wx", childprocess=False)
