import tempfile
import sys
PY3 = sys.version_info[0] >= 3
if PY3:
    TemporaryDirectory = tempfile.TemporaryDirectory
else:
    from pyscreenshot import tempdir27
    TemporaryDirectory = tempdir27.TemporaryDirectory27