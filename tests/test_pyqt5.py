from ref import backend_check


def test_pyqt5():
    backend_check('pyqt5', childprocess=True)
    backend_check('pyqt5', childprocess=False)
