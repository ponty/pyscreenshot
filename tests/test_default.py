from bt import backend_to_check


def test_default():
    # delay for freedesktop_dbus
    backend_to_check(None, delay=0.2)
