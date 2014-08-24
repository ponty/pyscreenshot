import pyscreenshot
from entrypoint2 import entrypoint


def print_name(name):
    print name, ' ' * (20 - len(name)),


@entrypoint
def print_versions():
    print_name('pyscreenshot')
    print pyscreenshot.__version__
    for name in pyscreenshot.backends():
        pyscreenshot.BACKEND_LOADER.force(name)
        print_name(name)
        try:
            x = pyscreenshot.BACKEND_LOADER.selected()
            print x.backend_version()
        except Exception:
            print 'missing'
