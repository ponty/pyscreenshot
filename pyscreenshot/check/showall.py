import time

import pyscreenshot
from entrypoint2 import entrypoint
from pyscreenshot import FailedBackendError, backends


@entrypoint
def show():
    im = []

    for x in backends():
        try:
            print("--> grabbing by " + x)
            im.append(pyscreenshot.grab(bbox=(500, 400, 800, 600), backend=x))
        except Exception as e:
            print(e)
    print(im)
    for x in im:
        x.show()
        time.sleep(1)
