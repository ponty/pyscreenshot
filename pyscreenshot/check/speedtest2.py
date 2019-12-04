import pyscreenshot
import tempfile
import time
import os


def run(force_backend, n, bbox=None):
    start = time.time()
    for _ in range(n):
        pyscreenshot.grab(
            bbox=bbox, backend=force_backend, childprocess=True)
    end = time.time()
    dt = end - start

    s = ''
    s += '%-20s' % force_backend
    s += '\t'
    s += '%-4.2g sec' % dt
    s += '\t'
    s += '(%5d ms per call)' % (1000.0 * dt / n)
    print(s)


def run_all(n, bbox=None):
    print('')

    s = ''
    s += 'n=%s' % n
    s += '\t'
    s += ' bounding box: {}'.format(bbox)
    print(s)

    print('------------------------------------------------------')

    for x in pyscreenshot.backends():
        try:
            run(x, n, bbox)
        except pyscreenshot.FailedBackendError as e:
            print(e)


def speedtest():
    n = 10
    run_all(n)
    run_all(n, (10, 10, 20, 20))


def main(virtual_display=False):
    if virtual_display:
        from pyvirtualdisplay import Display
        with Display(visible=0):
            speedtest()
    else:
        speedtest()


if __name__ == '__main__':
    main()
