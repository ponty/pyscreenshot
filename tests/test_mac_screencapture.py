from ref import backend_ref
from size import backend_size


def test_size_mac_screencapture():
    backend_size('mac_screencapture', virtual_display=False)
test_size_mac_screencapture.mac=1

def test_ref_mac_screencapture():
    backend_ref('mac_screencapture', virtual_display=False, ref='pil', x11=False)
test_ref_mac_screencapture.mac=1
