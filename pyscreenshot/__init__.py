import logging

from pyscreenshot.about import __version__
from pyscreenshot.childproc import childprocess_backend_version
from pyscreenshot.loader import FailedBackendError, backend_grab
from pyscreenshot.plugins import backend_dict

ADDITIONAL_IMPORTS = [FailedBackendError]

log = logging.getLogger(__name__)
log.debug("version=%s", __version__)


def grab(bbox=None, childprocess=None, backend=None):
    """Copy the contents of the screen to PIL image memory.

    :param bbox: optional bounding box (x1,y1,x2,y2)
    :param childprocess: run back-end in new process using popen. (bool)
        This can isolate back-ends from each other and from main process.
        It can be forced if set, otherwise childprocess is automatic.
    :param backend: back-end can be forced if set (examples:scrot, wx,..),
                    otherwise back-end is automatic
    """
    if bbox:
        x1, y1, x2, y2 = bbox
        if x2 <= x1:
            raise ValueError("bbox x2<=x1")
        if y2 <= y1:
            raise ValueError("bbox y2<=y1")
    return backend_grab(backend, bbox, childprocess)


def backends():
    """Back-end names as a list.

    :return: back-ends as string list
    """
    return list(backend_dict.keys())


def backend_version(backend):
    """Back-end version.

    :param backend: back-end (examples:scrot, wx,..)
    :return: version as string
    """
    return childprocess_backend_version(backend)
