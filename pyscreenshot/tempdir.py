import sys
import tempfile

PY2 = sys.version_info[0] == 2
if PY2:
    from pyscreenshot import tempdir27

    TemporaryDirectory = tempdir27.TemporaryDirectory27
else:
    TemporaryDirectory = tempfile.TemporaryDirectory
