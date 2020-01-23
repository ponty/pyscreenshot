import six

from ref import backend_check

if not six.PY2:
    def test_pyside2():
        backend_check('pyside2', childprocess=True)
        backend_check('pyside2', childprocess=False)
