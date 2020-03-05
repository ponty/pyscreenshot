import logging
import os

from pyscreenshot.imcodec import codec
from pyscreenshot.err import FailedBackendError
from pyscreenshot.util import proc
from pyscreenshot.tempdir import TemporaryDirectory

log = logging.getLogger(__name__)


def childprocess_backend_version(_backend_version, backend):
    return childprocess_backend_version_popen(backend)


def childprocess_backend_version_popen(backend):
    p = proc("pyscreenshot.cli.print_backend_version", [backend])
    if p.return_code != 0:
        log.error(p)
        raise FailedBackendError(p)

    return p.stdout


def childprocess_grab(_grab_simple, backend, bbox):
    return childprocess_grab_popen(backend, bbox)


def childprocess_grab_popen(backend, bbox):
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

        p = proc("pyscreenshot.cli.grab", cmd)
        if p.return_code != 0:
            # log.debug(p)
            raise FailedBackendError(p)

        data = open(filename, "rb").read()
        data = codec[1](data)
        return data
