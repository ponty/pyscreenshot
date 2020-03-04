from pyscreenshot.util import use_x_display

from ref import backend_to_check

if use_x_display():

    def test_imagemagick():
        backend_to_check("imagemagick")
