from entrypoint2 import entrypoint
import pyscreenshot
from pyscreenshot.imcodec import codec
import sys

@entrypoint
def main(backend):
    """Print pyscreenshot back-end version.

    :param backend: back-end (example:scrot, wx,..)
    """
    backend=backend if backend else None
    v = pyscreenshot.backend_version(backend=backend, childprocess=False)
    print(v)
    