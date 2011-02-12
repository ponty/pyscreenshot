from nose.tools import eq_
from pyscreenshot.backendloader import BackendLoader
from unittest import TestCase
import logging

logging.basicConfig(level=logging.DEBUG)


class Test(TestCase):
    
    def test_pref(self):
        man=BackendLoader()
        man.force(None)

        man.set_preference(['imagemagick', 'scrot'])
        eq_(man.selected().name, 'imagemagick')
        

        man.set_preference(['imagemagick','scrot', 'imagemagick'])
        eq_(man.selected().name, 'imagemagick')

        man.set_preference(['imagemagick'])
        eq_(man.selected().name, 'imagemagick')
        
        man.set_preference(['pygtk','imagemagick', 'scrot'])
        eq_(man.selected().name, 'pygtk')
        
        man.set_preference(['scrot', 'imagemagick'])
        eq_(man.selected().name, 'scrot')
        
        man.set_preference(['scrot','imagemagick', 'pygtk'])
        eq_(man.selected().name, 'scrot')
        
        man.set_preference(['scrot','imagemagick', 'scrot'])
        eq_(man.selected().name, 'scrot')

        man.set_preference(['scrot'])
        eq_(man.selected().name, 'scrot')
        
        
    def test_force(self):
        man=BackendLoader()
        for name in ['imagemagick', 'scrot', 'pygtk']:
            man.force(name)
            eq_(man.selected().name, name)
            man.force(None) # for other tests
        
    def test_mix(self):
        man=BackendLoader()
        man.force('scrot')
        man.set_preference(['imagemagick', 'scrot'])
        eq_(man.selected().name, 'scrot')
        
        
                          
        
        
        
        
        
