from pyscreenshot.iplugin import IPlugin
import logging
import plugins

log = logging.getLogger(__name__)


class PluginLoaderError(Exception):
    pass


class PluginLoader(object):
    def __init__(self, default_preference=[]):
        self.plugins = dict()

        self.all_names = [x.name for x in IPlugin.__subclasses__()]

        self.changed = True
        self._force_backend = None
        self.preference = []
        self.default_preference = default_preference
        self._backend = None

    def set_preference(self, x):
        self.changed = True
        self.preference = x

    def force(self, name):
        log.debug('forcing:' + str(name))
        self.changed = True
        self._force_backend = name

    @property
    def is_forced(self):
        return self._force_backend is not None

    @property
    def loaded_plugins(self):
        return self.plugins.values()

    def get_valid_plugin_by_name(self, name):
        if name not in self.plugins:
            ls = filter(lambda x: x.name == name, IPlugin.__subclasses__())
            if len(ls):
                try:
                    plugin = ls[0]()
                except Exception:
                    plugin = None
            else:
                plugin = None
            self.plugins[name] = plugin
        return self.plugins[name]

    def get_valid_plugin_by_list(self, ls):
        for name in ls:
            x = self.get_valid_plugin_by_name(name)
            if x:
                return x

    def selected(self):
        if self.changed:
            if self.is_forced:
                b = self.get_valid_plugin_by_name(self._force_backend)
                if not b:
                    raise PluginLoaderError('Forced backend not found, or cannot be loaded:' + self._force_backend)
            else:
                biglist = self.preference + self.default_preference + self.all_names
                b = self.get_valid_plugin_by_list(biglist)
                if not b:
                    self.raise_exc()
            self.changed = False
            self._backend = b
            log.debug('selecting plugin:' + self._backend.name)
        return self._backend

    def raise_exc(self):
        message = 'Install at least one backend!'
        raise PluginLoaderError(message)



