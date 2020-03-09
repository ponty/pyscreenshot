import logging

from pyscreenshot.about import __version__
from pyscreenshot.childproc import childprocess_backend_version, childprocess_grab
from pyscreenshot.loader import FailedBackendError, backend_grab, backend_version2
from pyscreenshot.plugins import backend_dict

ADDITIONAL_IMPORTS = [FailedBackendError]

log = logging.getLogger(__name__)
log.debug("version=%s", __version__)


def _grab_simple(backend=None, bbox=None, childprocess=False):
    # loader = Loader()
    # loader.force(backend)
    # backend_obj = loader.selected()
    # return backend_obj.grab(bbox)
    return backend_grab(backend, bbox, childprocess)


def _grab(childprocess, backend=None, bbox=None):
    if bbox:
        x1, y1, x2, y2 = bbox
        if x2 <= x1:
            raise ValueError("bbox x2<=x1")
        if y2 <= y1:
            raise ValueError("bbox y2<=y1")
    # if childprocess:
    #     log.debug('running "%s" in child process', backend)
    #     return childprocess_grab(_grab_simple, backend, bbox)
    # else:
    return _grab_simple(backend, bbox, childprocess)


# TODO: childprocess=None default
# TODO: static check: platform, version,...
def grab(bbox=None, childprocess=True, backend=None):
    """Copy the contents of the screen to PIL image memory.

    :param bbox: optional bounding box (x1,y1,x2,y2)
    :param childprocess: run back-end in new process using popen. 
        This can isolate back-ends from each other and from main process.
    :param backend: back-end can be forced if set (examples:scrot, wx,..),
                    otherwise back-end is automatic
    """
    return _grab(childprocess=childprocess, backend=backend, bbox=bbox)


def backends():
    """Back-end names as a list.

    :return: back-ends as string list
    """
    return backend_dict.keys()


def _backend_version(backend):
    # loader = Loader()
    # loader.force(backend)
    try:
        # x = loader.selected()
        # v = x.backend_version()
        v = backend_version2(backend)
    except Exception as e:
        log.warning(e)
        v = None
    return v


def backend_version(backend, childprocess=True):
    """Back-end version.

    :param backend: back-end (examples:scrot, wx,..)
    :param childprocess: see :py:func:`grab`
    :return: version as string
    """
    if not childprocess:
        return _backend_version(backend)
    else:
        return childprocess_backend_version(backend)
