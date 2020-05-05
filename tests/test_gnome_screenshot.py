from ref import backend_to_check, gnome, kde, prog_check

if gnome():

    if prog_check(["gnome-screenshot", "--version"]):

        def test_gnome_screenshot():
            assert not kde()
            # the flash effect can be seen on the next screenshot,
            # so some delay is needed
            backend_to_check("gnome-screenshot", delay=1)
