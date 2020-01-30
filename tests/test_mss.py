import six
from pyscreenshot import FailedBackendError

import x
from ref import backend_to_check

if not six.PY2:

    def test_mss():
        if x.missing_RANDR():
            try:
                backend_to_check("mss")
            except FailedBackendError:
                pass
        else:
            backend_to_check("mss")
