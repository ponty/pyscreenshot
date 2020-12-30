from bt import backend_to_check, gnome, kde

if gnome():

    def test_gnome_dbus():
        assert not kde()
        backend_to_check("gnome_dbus")
