import pyscreenshot
import tempfile
import time
import shutil


def run(force_backend, n):
    tmpdir = tempfile.mkdtemp(prefix='pyscreenshot_speedtest_')
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
    shutil.rmtree(tmpdir)


def run_all(n):
    print('')

    s = ''
    s += 'n=%s' % n
    print(s)

    print('------------------------------------------------------')

    for x in pyscreenshot.backends():
        try:
            run(x, n)
        except pyscreenshot.FailedBackendError as e:
            print(e)


def speedtest():
    n = 10
    run_all(n)


def main(virtual_display=False):
    if virtual_display:
        from pyvirtualdisplay import Display
        with Display(visible=0):
            speedtest()
    else:
        speedtest()


if __name__ == '__main__':
    main()
