import time

import pyscreenshot as ImageGrab
from pyscreenshot import FailedBackendError, backends


def show():
    im = []

    for x in backends():
        try:
            print("grabbing by " + x)
            im.append(
                ImageGrab.grab(bbox=(500, 400, 800, 600), backend=x, childprocess=True)
            )
        except FailedBackendError as e:
            print(e)
    print(im)
    for x in im:
        x.show()
        time.sleep(1)


if __name__ == "__main__":
    show()
