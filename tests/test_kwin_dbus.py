from bt import backend_to_check, gnome, kde

if kde():

    def test_kwin_dbus():
        assert not gnome()
        backend_to_check("kwin_dbus")
