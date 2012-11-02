from easyprocess import EasyProcess
from pyscreenshot.backendloader import BackendLoader
import Image
import logging
import tempfile

__version__ = '0.3.0'

log = logging.getLogger(__name__)
log.debug('version=' + __version__)


def grab(bbox=None, childprocess=False, backend=None):
    '''Copy the contents of the screen to PIL image memory.
    
    :param bbox: optional bounding box
    :param childprocess: pyscreenshot can cause an error, 
            if it is used on more different virtual displays 
            and back-end is not in different process.
            Some back-ends are always different processes: scrot, imagemagick
    :param backend: back-end can be forced if set (examples:scrot, wx,..), 
                    otherwise back-end is automatic
    '''
    if childprocess:
        f = tempfile.NamedTemporaryFile(suffix='.png', prefix='pyscreenshot_childprocess_')
        filename = f.name

        params = ["'%s'" % (filename), 'childprocess=False']
        if backend:
            params += ["backend='%s'" % (backend)]
        params = ','.join(params)

        EasyProcess(['python',
                     '-c',
                     "import pyscreenshot; pyscreenshot.grab_to_file(%s)" % params,
                     ]).check()
        im = Image.open(filename)
        if bbox:
            im = im.crop(bbox)
        return im
    else:
        if backend:
            BackendLoader().force(backend)
        return BackendLoader().selected().grab(bbox)


def grab_to_file(filename, childprocess=False, backend=None):
    '''Copy the contents of the screen to a file.
    
    :param filename: file for saving
    :param childprocess: see :py:func:`grab`
    :param backend: see :py:func:`grab`
    '''
    if childprocess:

        params = ["'%s'" % (filename), 'childprocess=False']
        if backend:
            params += ["backend='%s'" % (backend)]
        params = ','.join(params)

        EasyProcess(['python',
                     '-c',
                     "import pyscreenshot; pyscreenshot.grab_to_file(%s)" % params,
                     ]).check()
    else:
        if backend:
            BackendLoader().force(backend)
        return BackendLoader().selected().grab_to_file(filename)



