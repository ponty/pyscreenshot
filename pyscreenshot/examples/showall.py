from entrypoint2 import entrypoint
from pyscreenshot import backends
from pyscreenshot.loader import BackendLoaderError
import time

import pyscreenshot as ImageGrab


@entrypoint
def show():
    im = []

    for x in backends():
        try:
            print 'grabbing by ' + x
            im.append(ImageGrab.grab(bbox=(500, 400, 800, 600), backend=x))
        except BackendLoaderError as e:
            print e
    print im
    for x in im:
        x.show()
        time.sleep(1)
