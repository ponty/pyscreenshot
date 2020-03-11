import sys
import time

from entrypoint2 import entrypoint

import pyscreenshot
from pyscreenshot.util import proc


def run(force_backend, n, childprocess, bbox=None):
    sys.stdout.write("%-20s\t" % force_backend)
    sys.stdout.flush()  # before any crash

    try:
        start = time.time()
        for _ in range(n):
            pyscreenshot.grab(
                backend=force_backend, childprocess=childprocess, bbox=bbox
            )
        end = time.time()
        dt = end - start
        s = "%-4.2g sec\t" % dt
        s += "(%5d ms per call)" % (1000.0 * dt / n)
        sys.stdout.write(s)
    finally:
        print("")


# TODO: add default
def run_all(n, childprocess, virtual_only=True, bbox=None):
    print("")
    print("n=%s" % n)
    print("------------------------------------------------------")

    if bbox:
        x1, y1, x2, y2 = map(str, bbox)
        bbox = ":".join(map(str, (x1, y1, x2, y2)))
        bboxpar = ["--bbox", bbox]
    else:
        bboxpar = []
    for x in pyscreenshot.backends():
        if virtual_only and x == "gnome-screenshot":  # TODO: remove
            continue
        if childprocess:
            try:
                run(x, n, True, bbox=bbox)
            except Exception:
                pass
        else:
            p = proc("pyscreenshot.check.speedtest", ["--backend", x] + bboxpar)
            print(p.stdout)


@entrypoint
def speedtest(virtual_display=False, backend="", childprocess=False, bbox=""):
    """Performance test of all back-ends. 
    
    :param virtual_display: run with Xvfb
    :param bbox: bounding box coordinates x1:y1:x2:y2
    :param backend: back-end can be forced if set (example:scrot, wx,..),
                    otherwise back-end is automatic
    :param childprocess: pyscreenshot parameter childprocess
    """
    n = 10
    if bbox:
        x1, y1, x2, y2 = map(int, bbox.split(":"))
        bbox = x1, y1, x2, y2
    else:
        bbox = None

    def f(virtual_only):
        if backend:
            try:
                run(backend, n, childprocess, bbox=bbox)
            except pyscreenshot.FailedBackendError:
                pass
        else:
            run_all(n, childprocess, virtual_only=virtual_only, bbox=bbox)

    if virtual_display:
        from pyvirtualdisplay import Display

        with Display(visible=0):
            f(virtual_only=True)
    else:
        f(virtual_only=False)
