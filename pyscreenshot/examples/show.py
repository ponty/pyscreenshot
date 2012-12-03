from entrypoint2 import entrypoint
from pyscreenshot import grab


@entrypoint
def show(backend='auto'):
    if backend == 'auto':
        backend = None
    im = grab(bbox=(100, 200, 300, 400), backend=backend)
    im.show()
