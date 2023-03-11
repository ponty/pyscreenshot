import sys
import time

from entrypoint2 import entrypoint

import pyscreenshot
from pyscreenshot.plugins.freedesktop_dbus import FreedesktopDBusWrapper
from pyscreenshot.plugins.gnome_dbus import GnomeDBusWrapper
from pyscreenshot.plugins.gnome_screenshot import GnomeScreenshotWrapper
from pyscreenshot.plugins.kwin_dbus import KwinDBusWrapper
from pyscreenshot.util import run_mod_as_subproc


def run(force_backend, n, childprocess, bbox=None):
    sys.stdout.write("%-20s\t" % force_backend)
    sys.stdout.flush()  # before any crash
    # if force_backend == "freedesktop_dbus":
    #     return
    if force_backend == "default":
        force_backend = None
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


novirt = [
    GnomeDBusWrapper.name,
    KwinDBusWrapper.name,
    GnomeScreenshotWrapper.name,
    FreedesktopDBusWrapper.name,
]


def run_all(n, childprocess_param, virtual_only=True, bbox=None):
    debug = True
    print("")
    print("n=%s" % n)
    print("------------------------------------------------------")

    if bbox:
        x1, y1, x2, y2 = map(str, bbox)
        bbox = ":".join(map(str, (x1, y1, x2, y2)))
        bboxpar = ["--bbox", bbox]
    else:
        bboxpar = []
    if debug:
        debugpar = ["--debug"]
    else:
        debugpar = []
    for x in ["default"] + pyscreenshot.backends():
        if x == "freedesktop_dbus":
            continue
        backendpar = ["--backend", x]
        # skip non X backends
        if virtual_only and x in novirt:
            continue
        p = run_mod_as_subproc(
            "pyscreenshot.check.speedtest",
            ["--childprocess", childprocess_param, "--number", str(n)]
            + bboxpar
            + debugpar
            + backendpar,
        )
        print(p.stdout)


@entrypoint
def speedtest(virtual_display=False, backend="", childprocess="", bbox="", number=10):
    """Performance test of all back-ends.

    :param virtual_display: run with Xvfb
    :param bbox: bounding box coordinates x1:y1:x2:y2
    :param backend: back-end can be forced if set (example:default, scrot, wx,..),
                    otherwise all back-ends are tested
    :param childprocess: pyscreenshot parameter childprocess (0/1)
    :param number: number of screenshots for each backend (default:10)
    """
    childprocess_param = childprocess
    if childprocess == "":
        childprocess = True  # default
    elif childprocess == "0":
        childprocess = False
    elif childprocess == "1":
        childprocess = True
    else:
        raise ValueError("invalid childprocess value")

    if bbox:
        x1, y1, x2, y2 = map(int, bbox.split(":"))
        bbox = x1, y1, x2, y2
    else:
        bbox = None

    def f(virtual_only):
        if backend:
            try:
                run(backend, number, childprocess, bbox=bbox)
            except pyscreenshot.FailedBackendError:
                pass
        else:
            run_all(number, childprocess_param, virtual_only=virtual_only, bbox=bbox)

    if virtual_display:
        from pyvirtualdisplay import Display

        with Display(visible=0):
            f(virtual_only=True)
    else:
        f(virtual_only=False)
