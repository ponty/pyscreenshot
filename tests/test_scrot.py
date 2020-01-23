from ref import backend_check


def test_scrot():
    backend_check('scrot', ref='imagemagick', childprocess=True)
    backend_check('scrot', ref='imagemagick', childprocess=False)
