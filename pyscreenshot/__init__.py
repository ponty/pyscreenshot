from path import path
from yapsy.PluginManager import PluginManager
import logging

#from version import __version__

__version__='0.1.1'

def get_plugin(backend_preference=None, force_backend=None):    
    places = [path(__file__).dirname()]
    ext = 'conf'

    pm = PluginManager()
    pm.setPluginInfoExtension(ext)
    pm.setPluginPlaces(places)
    pm.collectPlugins()
    
    if force_backend:
        return pm.activatePluginByName(force_backend)
        
    if backend_preference:
        for x in backend_preference:
            plugin = pm.activatePluginByName(x)
            if plugin:
                if plugin.is_available:
                    return plugin
    
    # get first
    all = pm.getAllPlugins()
    for x in all:
        plugin = pm.activatePluginByName(x.name)
        if plugin.is_available:
            return plugin

default_backend_preference=['pil', 'scrot']
def grab(bbox=None, backend_preference=default_backend_preference, force_backend=None):  
    x = get_plugin(backend_preference=backend_preference, force_backend=force_backend)
    if not x:
        raise(Exception('no plugin found!'))
    return x.grab(bbox)

def grab_to_file(filename, backend_preference=default_backend_preference, force_backend=None):  
    x = get_plugin(backend_preference=backend_preference, force_backend=force_backend)
    if not x:
        raise(Exception('no plugin found!'))
    return x.grab_to_file(filename)



