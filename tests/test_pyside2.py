import six

from ref import backend_to_check, check_import

if not six.PY2 and check_import("PySide2"):

    def test_pyside2():
        backend_to_check("pyside2")
