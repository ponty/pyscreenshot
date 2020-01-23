import six

from ref import backend_check

# no pygtk for py3
if six.PY2:

    def test_pygtk():
        backend_check("pygtk", childprocess=True)
        backend_check("pygtk", childprocess=False)
