from ref import backend_check


def test_imagemagick():
    backend_check('imagemagick', childprocess=True)
    backend_check('imagemagick', childprocess=False)
