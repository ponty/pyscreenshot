import time

import pyscreenshot as ImageGrab
from entrypoint2 import entrypoint
from pyscreenshot import FailedBackendError, backends


@entrypoint
def show():
    im = []

    for x in backends():
        try:
            print("--> grabbing by " + x)
            im.append(
                ImageGrab.grab(bbox=(500, 400, 800, 600), backend=x, childprocess=True)
            )
        except Exception as e:
            print(e)
    print(im)
    for x in im:
        x.show()
        time.sleep(1)
