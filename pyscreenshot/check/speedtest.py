import sys
import time

from entrypoint2 import entrypoint

import pyscreenshot
from pyscreenshot.procutil import proc


def run(force_backend, n, childprocess):
    sys.stdout.write("%-20s\t" % force_backend)
    sys.stdout.flush()  # before any crash

    try:
        start = time.time()
        for _ in range(n):
            pyscreenshot.grab(backend=force_backend, childprocess=childprocess)
        end = time.time()
        dt = end - start
        s = "%-4.2g sec\t" % dt
        s += "(%5d ms per call)" % (1000.0 * dt / n)
        sys.stdout.write(s)
    finally:
        print("")


def run_all(n, childprocess, virtual_only=True):
    print("")
    print("n=%s" % n)
    print("------------------------------------------------------")

    for x in pyscreenshot.backends():
        if virtual_only and x == "gnome-screenshot":
            continue
        if childprocess:
            try:
                run(x, n, True)
            except pyscreenshot.FailedBackendError:
                pass
        else:
            p = proc("pyscreenshot.check.speedtest", ["--backend", x])
            print(p.stdout)


@entrypoint
def speedtest(virtual_display=False, backend="", childprocess=False):
    n = 10

    def f(virtual_only):
        if backend:
            try:
                run(backend, n, childprocess)
            except pyscreenshot.FailedBackendError:
                pass
        else:
            run_all(n, childprocess, virtual_only=virtual_only)

    if virtual_display:
        from pyvirtualdisplay import Display

        with Display(visible=0):
            f(virtual_only=True)
    else:
        f(virtual_only=False)
