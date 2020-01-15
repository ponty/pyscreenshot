from ref import backend_ref
from size import backend_size


def test_size_pil():
    backend_size('pil', virtual_display=False)
test_size_pil.mac=1

# TODO: fix test
# def test_ref_pil():
#     backend_ref('pil', virtual_display=False, ref='pil', x11=False)
# test_ref_pil.mac=1
