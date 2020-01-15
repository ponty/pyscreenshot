from ref import backend_ref
from size import backend_size


def test_size_mac_quartz():
    backend_size('mac_quartz', virtual_display=False, childprocess=False)
test_size_mac_quartz.mac=1

# TODO: fix test
# def test_ref_mac_quartz():
#     backend_ref('mac_quartz', virtual_display=False, ref='pil', x11=False, childprocess=False)
# test_ref_mac_quartz.mac=1
