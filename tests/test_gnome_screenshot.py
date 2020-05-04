from pyscreenshot.util import use_x_display
import os
from ref import backend_to_check, check_import, gnome, kde

if gnome():

    def test_gnome_screenshot():
        assert not kde()

        # the flash effect can be seen on the next screenshot,
        # so some delay is needed
        backend_to_check("gnome-screenshot", delay=1)
