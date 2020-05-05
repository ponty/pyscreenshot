import six

from ref import backend_to_check, check_import

# no pygtk for py3
if six.PY2 and check_import("gtk"):

    def test_pygtk():
        backend_to_check("pygtk")
