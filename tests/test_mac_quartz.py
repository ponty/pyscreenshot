from ref import backend_ref
from size import backend_size


def test_size_mac_quartz():
    backend_size('mac_quartz', virtual_display=False, childprocess=False)
test_size_mac_quartz.mac=1