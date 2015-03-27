import pyscreenshot
from entrypoint2 import entrypoint


def print_name_version(name, version):
    s= '%-20s %s' % (name, version)
    print(s)


@entrypoint
def print_versions():
    print_name_version('pyscreenshot', pyscreenshot.__version__)
    for name in pyscreenshot.backends():
        pyscreenshot.BACKEND_LOADER.force(name)
        try:
            x = pyscreenshot.BACKEND_LOADER.selected()
            v= x.backend_version()
        except Exception:
            v= 'missing'
        print_name_version(name, v)
