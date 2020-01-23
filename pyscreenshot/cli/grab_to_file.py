from entrypoint2 import entrypoint

import pyscreenshot
from pyscreenshot.imcodec import codec


@entrypoint
def main(filename, x1, y1, x2, y2, backend=""):
    """Copy the contents of the screen to file. 
    Full screen is selected if bounding box coordinates are zero: 0,0,0,0

    :param filename: output file
    :param x1: bounding box coordinates
    :param y1: bounding box coordinates
    :param x2: bounding box coordinates
    :param y2: bounding box coordinates
    :param backend: back-end can be forced if set (example:scrot, wx,..),
                    otherwise back-end is automatic
    """
    backend = backend if backend else None

    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

    bbox = None
    if x1 or y1 or x2 or y2:
        bbox = x1, y1, x2, y2

    im = pyscreenshot.grab(bbox=bbox, childprocess=False, backend=backend)
    b = codec[0](im)
    with open(filename, "wb") as f:
        f.write(b)
