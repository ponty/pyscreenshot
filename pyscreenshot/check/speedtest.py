import pyscreenshot
import tempfile
import time
import shutil


def run(force_backend, n):
    start = time.time()
    for _ in range(n):
        pyscreenshot.grab(
            backend=force_backend, childprocess=True)
    end = time.time()
    dt = end - start

    s = ''
    s += '%-20s' % force_backend
    s += '\t'
    s += '%-4.2g sec' % dt
    s += '\t'
    s += '(%5d ms per call)' % (1000.0 * dt / n)
    print(s)


def run_all(n, virtual_only=True):
    print('')

    s = ''
    s += 'n=%s' % n
    print(s)

    print('------------------------------------------------------')

    for x in pyscreenshot.backends():
        if virtual_only and x == 'gnome-screenshot':
            continue
        try:
            run(x, n)
        except pyscreenshot.FailedBackendError as e:
            print(e)


def speedtest(virtual_display=False):
    n = 10
    if virtual_display:
        from pyvirtualdisplay import Display
        with Display(visible=0):
            run_all(n, virtual_only=True)
    else:
        run_all(n, virtual_only=False)


if __name__ == '__main__':
    speedtest()
