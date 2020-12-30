import logging
import os
from tempfile import TemporaryDirectory

from pyscreenshot.err import FailedBackendError
from pyscreenshot.imcodec import codec
from pyscreenshot.util import run_mod_as_subproc

log = logging.getLogger(__name__)


def childprocess_backend_version(backend):
    p = run_mod_as_subproc("pyscreenshot.cli.print_backend_version", [backend])
    if p.return_code != 0:
        log.warning(p)
        raise FailedBackendError(p)

    return p.stdout


def childprocess_grab(backend, bbox):
    with TemporaryDirectory(prefix="pyscreenshot") as tmpdirname:
        filename = os.path.join(tmpdirname, "screenshot.png")
        cmd = ["--filename", filename]
        if bbox:
            x1, y1, x2, y2 = map(str, bbox)
            bbox = ":".join(map(str, (x1, y1, x2, y2)))
            cmd += ["--bbox", bbox]
        if backend:
            cmd += ["--backend", backend]
        if log.isEnabledFor(logging.DEBUG):
            cmd += ["--debug"]

        p = run_mod_as_subproc("pyscreenshot.cli.grab", cmd)
        if p.return_code != 0:
            # log.debug(p)
            raise FailedBackendError(p)

        data = open(filename, "rb").read()
        data = codec[1](data)
        return data
