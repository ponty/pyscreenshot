from bt import backend_to_check, gnome, gnome_version, kde

if gnome():
    # GNOME Shell 41.0 disallowed unrestricted access to the screenshot API
    if gnome_version()[0] < 41:

        def test_gnome_dbus():
            assert not kde()
            backend_to_check("gnome_dbus")
