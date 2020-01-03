from ref import backend_ref
from size import backend_size
import six

if not six.PY2:

    def test_size_pyside2():
        backend_size('pyside2')


    def test_ref_pyside2():
        backend_ref('pyside2')
