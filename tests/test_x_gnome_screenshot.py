from bt import backend_to_check, gnome, kde, prog_check

# 'gnome-screenshot' makes strange effects on screen.
# It can disturb later tests.
# Make this test the last by starting the name with 'x'
if gnome():

    if prog_check(["gnome-screenshot", "--version"]):

        def test_gnome_screenshot():
            assert not kde()
            # the flash effect can be seen on the next screenshot,
            # so some delay is needed
            backend_to_check("gnome-screenshot", delay=1)
