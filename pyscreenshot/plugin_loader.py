from yapsy.PluginManager import PluginManager
import logging
from path import path
import platform
log=logging.getLogger(__name__)

def get_plugin(backend_preference=None, force_backend=None):    
    places = [path(__file__).dirname()]
    ext = 'conf'

    pm = PluginManager()
    pm.setPluginInfoExtension(ext)
    pm.setPluginPlaces(places)
    pm.collectPlugins()

    all = pm.getAllPlugins()
    for x in all:
        x.plugin_object.name = x.name
    
    if force_backend:
        return pm.activatePluginByName(force_backend)
    
    if backend_preference:
        def key(x):
            if x.name in backend_preference:
                return backend_preference.index(x.name)
            return 1000
        log.debug('before sort:')
        log.debug([x.name for x in all])
        all.sort(key=key)
        log.debug('after sort:')
        log.debug([x.name for x in all])

    # get first
    for x in all:
        plugin = pm.activatePluginByName(x.name)
        #if plugin.is_available:
        return plugin
    
    if not len(all):
        raise(Exception('no plugin found!'))
        
    
    message = 'Install at least one backend!' 
    for x in all:
        message += '\n'
        message += '[%s]' % (x.name)
        if hasattr(x.plugin_object, 'home_url'):
            home_url = x.plugin_object.home_url
            message += '\n'
            message += '%s' % (home_url)
        message += '\n'
        if platform.dist()[0].lower() == 'ubuntu':
            message += 'You can install it in terminal:'
            message += '\n'
            message += '\t'
            message += 'sudo apt-get install %s' % x.plugin_object.ubuntu_package
    raise Exception(message)
