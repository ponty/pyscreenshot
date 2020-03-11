from pyscreenshot.util import use_x_display
import os
from ref import backend_to_check, check_import, gnome, kde
from nose.tools import eq_

if gnome():

    def test_gnome_dbus():
        eq_(kde(), False)
        backend_to_check("gnome_dbus")

