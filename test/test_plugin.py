from pyscreenshot import get_plugin
from unittest import TestCase


class Test(TestCase):
    def test_pref(self):
        self.assertEquals(get_plugin(backend_preference=['imagemagick', 'scrot']).name, 'imagemagick')
        self.assertEquals(get_plugin(backend_preference=['scrot', 'imagemagick']).name, 'scrot')
        self.assertEquals(get_plugin(backend_preference=['imagemagick']).name, 'imagemagick')
        self.assertEquals(get_plugin(backend_preference=['scrot']).name, 'scrot')
        self.assertEquals(get_plugin(backend_preference=['scrot','imagemagick', 'scrot']).name, 'scrot')
        self.assertEquals(get_plugin(backend_preference=['imagemagick','scrot', 'imagemagick']).name, 'imagemagick')
        
    def test_force(self):
        for name in ['imagemagick', 'scrot']:
            p = get_plugin(force_backend=name)
            self.assertEquals(p.name, name)
        
        
        
        
        
        
        
        
        
