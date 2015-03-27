from entrypoint2 import entrypoint
import pyscreenshot
import tempfile
import time


def run(force_backend, n, to_file, bbox=None):
    f = tempfile.NamedTemporaryFile(suffix='.png', prefix='test')
    filename = f.name
    start = time.time()
    for i in range(n):
        if to_file:
            pyscreenshot.grab_to_file(filename, backend=force_backend)
        else:
            pyscreenshot.grab(bbox=bbox, backend=force_backend)
    end = time.time()
    dt = end - start

    s = ''
    s += '%-20s' % force_backend
    s += '\t'
    s += '%-4.2g sec' % dt
    s += '\t'
    s += '(%5d ms per call)' % (1000.0 * dt / n)
    print(s)


def run_all(n, to_file, bbox=None):
    print('')

    s = ''
    s += 'n=%s' % n
    s += '\t'
    s += ' to_file: %s' % to_file
    s += '\t'
    s += ' bounding box: %s' % (bbox,)
    print(s)

    print('------------------------------------------------------')

    for x in pyscreenshot.backends():
        try:
            run(x, n, to_file, bbox)
        except pyscreenshot.FailedBackendError as e:
            print(e)


@entrypoint
def speedtest():
    n = 10
    run_all(n, True)
    run_all(n, False)
    run_all(n, False, (10, 10, 20, 20))
