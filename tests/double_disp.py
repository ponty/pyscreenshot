import sys

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay import Display


def check_double_disp(backend):
    python = sys.executable

    # the main process may crash,
    # so it must be tested in subprocess
    cmd = [python, __file__, backend, "--debug"]
    p = EasyProcess(cmd).call()
    assert p.return_code == 0


@entrypoint
def main(backend):
    import os
    import sys

    sys.path.append(os.getcwd())
    from pyscreenshot import grab

    with Display(visible=False):
        img = grab(backend=backend)
        assert img

    with Display(visible=False):
        img = grab(backend=backend)
        assert img
