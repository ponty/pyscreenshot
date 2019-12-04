from ref import backend_ref
from size import backend_size
import six

# no pygtk for py3
if six.PY2:

    def test_size_pygtk():
        backend_size('pygtk')
    
    
    def test_ref_pygtk():
        backend_ref('pygtk')
