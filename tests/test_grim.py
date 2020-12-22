from bt import backend_to_check, prog_check
from pyscreenshot.util import use_x_display

if not use_x_display():
    if prog_check(["grim", "-h"]):

        def test_grim():
            backend_to_check("grim")
