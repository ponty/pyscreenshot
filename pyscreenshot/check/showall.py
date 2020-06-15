import time

from entrypoint2 import entrypoint

import pyscreenshot
from pyscreenshot import backends


@entrypoint
def show():
    im = []
    blist = []

    for x in backends():
        try:
            print("--> grabbing by " + x)
            im.append(pyscreenshot.grab(bbox=(500, 400, 800, 600), backend=x))
            blist.append(x)
        except Exception as e:
            print(e)
    print(im)
    print(blist)
    for x in im:
        x.show()
        time.sleep(0.5)
