import os

from bt import backend_to_check

PYSCREENSHOT_TEST_FREEDESKTOP_DBUS = os.environ.get(
    "PYSCREENSHOT_TEST_FREEDESKTOP_DBUS"
)

if PYSCREENSHOT_TEST_FREEDESKTOP_DBUS:

    def test_freedesktop_dbus():
        # the previous confirmation dialog can be seen on the next screenshot,
        # so some delay is needed
        # 0.1 is not enough
        backend_to_check("freedesktop_dbus", delay=0.2)
