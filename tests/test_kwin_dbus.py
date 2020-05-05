import os

from pyscreenshot.util import use_x_display
from ref import backend_to_check, check_import, gnome, kde

if kde():

    def test_kwin_dbus():
        assert not gnome()
        backend_to_check("kwin_dbus")
