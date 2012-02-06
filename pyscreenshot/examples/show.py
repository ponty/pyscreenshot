from entrypoint2 import entrypoint
from pyscreenshot import grab
from pyscreenshot.backendloader import BackendLoader

@entrypoint
def show(backend='auto'):
    if backend!='auto':
        BackendLoader().force(backend)
    im = grab(bbox=(100, 200, 300, 400))
    im.show()

