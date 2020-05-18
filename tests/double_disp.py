import os
import sys

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay import Display


def check_double_disp(backend):
    python = sys.executable
    if not backend:
        backend = ""

    # the main process may crash,
    # so it must be tested in subprocess
    fname = __file__.rsplit(".", 1)[0] + ".py"
    cmd = [python, fname, backend, "--debug"]
    p = EasyProcess(cmd).call()
    assert p.return_code == 0


@entrypoint
def main(backend):
    if not backend:
        backend = None

    sys.path.append(os.getcwd())
    from pyscreenshot import grab

    with Display(visible=False):
        img = grab(backend=backend)
        assert img

    with Display(visible=False):
        img = grab(backend=backend)
        assert img
