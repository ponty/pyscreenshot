from ref import backend_check


def test_pyside():
    backend_check("pyside", childprocess=True)
    backend_check("pyside", childprocess=False)
