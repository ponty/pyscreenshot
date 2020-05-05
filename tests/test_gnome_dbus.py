import os

from pyscreenshot.util import use_x_display
from ref import backend_to_check, check_import, gnome, kde

if gnome():

    def test_gnome_dbus():
        assert not kde()
        backend_to_check("gnome_dbus")
