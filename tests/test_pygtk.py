import six

from ref import backend_to_check

# no pygtk for py3
if six.PY2:

    def test_pygtk():
        backend_to_check("pygtk")
