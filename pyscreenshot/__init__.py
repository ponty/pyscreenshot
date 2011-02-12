from pyscreenshot.backendloader import BackendLoader
import logging

__version__ = '0.1.4'

log = logging.getLogger(__name__)
log.debug('version=' + __version__)

def grab(bbox=None):  
    return BackendLoader().selected().grab(bbox)

def grab_to_file(filename):  
    return BackendLoader().selected().grab_to_file(filename)



