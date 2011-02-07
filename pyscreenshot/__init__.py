from path import path
from pyscreenshot.plugin_loader import get_plugin
from yapsy.PluginManager import PluginManager
import logging
import platform

__version__ = '0.1.4'

log=logging.getLogger(__name__)

default_backend_preference = ['pil', 'scrot', 'pygtk', 'imagemagick']
def grab(bbox=None, backend_preference=default_backend_preference, force_backend=None):  
    x = get_plugin(backend_preference=backend_preference, force_backend=force_backend)
    assert x, 'no plugin for (backend_preference={backend_preference}, force_backend={force_backend})'.format(
        backend_preference=backend_preference, 
        force_backend=force_backend)
    return x.grab(bbox)

def grab_to_file(filename, backend_preference=default_backend_preference, force_backend=None):  
    x = get_plugin(backend_preference=backend_preference, force_backend=force_backend)
    assert x, 'no plugin for (backend_preference={backend_preference}, force_backend={force_backend})'.format(
        backend_preference=backend_preference, 
        force_backend=force_backend)
    return x.grab_to_file(filename)



