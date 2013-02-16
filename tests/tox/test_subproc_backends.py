from compare import backend_size, backend_ref


def test_scrot():
    backend='scrot'
    backend_size(backend)
    backend_ref(backend)
    
def test_imagemagick():
    backend='imagemagick'
    backend_size(backend)
    backend_ref(backend)
