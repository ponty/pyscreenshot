from ref import backend_check
import six

if not six.PY2:
    def test_pyside2():
        backend_check('pyside2', childprocess=True)
        backend_check('pyside2', childprocess=False)
