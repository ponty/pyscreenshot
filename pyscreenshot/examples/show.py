from pyscreenshot import grab
from entrypoint2 import entrypoint

@entrypoint
def show():
    im = grab(bbox=(100, 200, 300, 400))
    im.show()

