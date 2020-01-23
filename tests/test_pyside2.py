import six

from ref import backend_to_check

if not six.PY2:

    def test_pyside2():
        backend_to_check("pyside2")
