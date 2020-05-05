from pyscreenshot.util import py2
from ref import backend_to_check, gnome, kde

# no jeepney for py2
if kde() and not py2():

    def test_kwin_dbus():
        assert not gnome()
        backend_to_check("kwin_dbus")
