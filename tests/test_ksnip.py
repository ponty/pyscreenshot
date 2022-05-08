from bt import backend_to_check, prog_check

from pyscreenshot.util import use_x_display

if prog_check(["ksnip", "--version"]):

    def test_scrot():
        backend_to_check("scrot")
