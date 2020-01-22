from ref import backend_check
import six

# no pygtk for py3
if six.PY2:

    def test_pygtk():
        backend_check('pygtk', childprocess=True)
        backend_check('pygtk', childprocess=False)
