import tempfile

from pyscreenshot.util import py2

if py2():
    from pyscreenshot import tempdir27

    TemporaryDirectory = tempdir27.TemporaryDirectory27
else:
    TemporaryDirectory = tempfile.TemporaryDirectory
