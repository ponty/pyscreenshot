from pyscreenshot.util import use_x_display
import os
from ref import backend_to_check, check_import, kde, gnome

if kde():

    def test_kwin_dbus():
        assert not gnome()
        backend_to_check("kwin_dbus")
