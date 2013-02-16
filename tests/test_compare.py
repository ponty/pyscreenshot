from tox.compare import backend_size, backend_ref

    
def test_pygtk():
    backend='pygtk'
    backend_size(backend)
    backend_ref(backend)
    
def test_wx():
    backend='wx'
    backend_size(backend)
    backend_ref(backend)
    
    
    
    