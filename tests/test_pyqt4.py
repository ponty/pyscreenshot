from ref import backend_check




def test_pyqt4():
    backend_check('pyqt', childprocess=True)
    backend_check('pyqt', childprocess=False)
