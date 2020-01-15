from ref import backend_ref
from size import backend_size


def test_size_scrot():
    backend_size('scrot')


def test_ref_scrot():
    backend_ref('scrot', ref='imagemagick')
