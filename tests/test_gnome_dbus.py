from pyscreenshot.util import py2
from ref import backend_to_check, gnome, kde

# no jeepney for py2
if gnome() and not py2():

    def test_gnome_dbus():
        assert not kde()
        backend_to_check("gnome_dbus")
