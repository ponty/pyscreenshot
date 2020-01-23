from ref import backend_check


def test_pygdk3():
    backend_check("pygdk3", childprocess=True)
    backend_check("pygdk3", childprocess=False)
