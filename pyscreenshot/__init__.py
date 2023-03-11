import logging
from typing import List, Optional, Tuple

from PIL import Image

from pyscreenshot.about import __version__
from pyscreenshot.childproc import childprocess_backend_version
from pyscreenshot.loader import FailedBackendError, backend_dict, backend_grab

ADDITIONAL_IMPORTS = [FailedBackendError]

log = logging.getLogger(__name__)
log.debug("version=%s", __version__)


def grab(
    bbox: Optional[Tuple[int, int, int, int]] = None,
    childprocess: bool = True,
    backend: Optional[str] = None,
) -> "Image":
    """Copy the contents of the screen to PIL image memory.

    :param bbox: optional bounding box (x1,y1,x2,y2)
    :param childprocess: run back-end in new process using popen. (bool)
        This isolates back-ends from each other and from main process.
        Leave it as it is (True) to have a safe setting.
        Set it False to improve performance, but then conflicts are possible.
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


def backends() -> List[str]:
    """Back-end names as a list.

    :return: back-ends as string list
    """
    return list(backend_dict.keys())


def backend_version(backend: str) -> str:
    """Back-end version.

    :param backend: back-end (examples:scrot, wx,..)
    :return: version as string
    """
    return childprocess_backend_version(backend)
