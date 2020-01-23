from size import backend_size

# DISPLAY variable doesn't work -> no Xvfb


def test_size_gnome_screenshot():
    backend_size("gnome-screenshot", childprocess=True)
    backend_size("gnome-screenshot", childprocess=False)


test_size_gnome_screenshot.real_disp_only = 1

# TODO:how to call it on static screen?
# def test_ref_gnome_screenshot():
#     backend_ref('gnome-screenshot',  childprocess=True)
#     backend_ref('gnome-screenshot',  childprocess=False)
