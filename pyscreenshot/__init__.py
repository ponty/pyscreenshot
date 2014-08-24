from PIL import Image
from easyprocess import EasyProcess
import logging
from pyscreenshot.loader import Loader, FailedBackendError
import sys
import tempfile


__version__ = '0.3.3'

log = logging.getLogger(__name__)
log.debug('version=' + __version__)

BACKEND_LOADER = None


def _get_loader():
    global BACKEND_LOADER
    if not BACKEND_LOADER:
        BACKEND_LOADER = Loader()
    return BACKEND_LOADER


def _grab(to_file, childprocess=False, backend=None, bbox=None, filename=None):
    if childprocess:
        log.debug('running "%s" in child process' % backend)

        if not to_file:
            f = tempfile.NamedTemporaryFile(
                suffix='.png', prefix='pyscreenshot_childprocess_')
            filename = f.name

        params = ["'%s'" % (filename), 'childprocess=False']
        if backend:
            params += ["backend='%s'" % (backend)]
        params = ','.join(params)

        EasyProcess([sys.executable,
                     '-c',
                     'import pyscreenshot; pyscreenshot.grab_to_file(%s)' % (
                         params),
                     ]).check()
        if not to_file:
            im = Image.open(filename)
            if bbox:
                im = im.crop(bbox)
            return im
    else:
        if backend:
            _get_loader().force(backend)
        backend_obj = _get_loader().selected()

        if to_file:
            return backend_obj.grab_to_file(filename)
        else:
            return backend_obj.grab(bbox)


def grab(bbox=None, childprocess=False, backend=None):
    """Copy the contents of the screen to PIL image memory.

    :param bbox: optional bounding box (x1,y1,x2,y2)
    :param childprocess: pyscreenshot can cause an error,
            if it is used on more different virtual displays
            and back-end is not in different process.
            Some back-ends are always different processes: scrot, imagemagick
    :param backend: back-end can be forced if set (examples:scrot, wx,..),
                    otherwise back-end is automatic

    """
    return _grab(to_file=False, childprocess=childprocess, backend=backend, bbox=bbox)


def grab_to_file(filename, childprocess=False, backend=None):
    """Copy the contents of the screen to a file.

    :param filename: file for saving
    :param childprocess: see :py:func:`grab`
    :param backend: see :py:func:`grab`

    """
    return _grab(to_file=True, childprocess=childprocess, backend=backend, filename=filename)


def backends():
    '''Back-end names as a list'''
    return _get_loader().all_names
