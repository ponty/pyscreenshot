from pyscreenshot.util import use_x_display
import os
from ref import backend_to_check, check_import, kde, gnome
from nose.tools import eq_

if kde():

    def test_kwin_dbus():
        eq_(gnome(), False)
        backend_to_check("kwin_dbus")

