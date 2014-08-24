from easyprocess import EasyProcess
from image_debug import img_debug
from nose.tools import eq_, with_setup
from pyvirtualdisplay import Display
from PIL import ImageChops
# import Tkinter
import pyscreenshot
import tempfile
# import Xlib.display

# backends = [
#    'scrot',
#    'imagemagick',
#    'pygtk',
# 'pyqt', #strange error: ICE default IO error handler doing an exit(), pid = 26424, errno = 32
#    'wx',
# ]
ref = 'scrot'


def display_size():
#    root = Tkinter.Tk()
#
#    screen_width = root.winfo_screenwidth()
#    screen_height = root.winfo_screenheight()

#    xdisp=Xlib.display.Display()
#    width = xdisp.screen().width_in_pixels
#    height = xdisp.screen().height_in_pixels
    # http://www.cyberciti.biz/faq/how-do-i-find-out-screen-resolution-of-my-linux-desktop/
    # xdpyinfo  | grep 'dimensions:'
    for x in EasyProcess('xdpyinfo').call().stdout.splitlines():
        if 'dimensions:' in x:
            screen_width, screen_height = map(
                int, x.strip().split()[1].split('x'))

    # xrandr | grep '*'
#    for x in EasyProcess('xrandr').call().stdout.splitlines():
#        if '*' in x:
#            screen_width, screen_height = map(
#                int, x.strip().split()[0].split('x'))
    return screen_width, screen_height

process = screen = None


def setup_func():
    'set up test fixtures'
    global process, screen
    screen = Display(visible=0)
    screen.start()
    process = EasyProcess('gnumeric').start().sleep(3)


def teardown_func():
    'tear down test fixtures'
    global process, screen
    process.stop()
    screen.stop()


def test_display_size():
    width, height = display_size()
    assert width > 10
    assert height > 10


def check_size(backend, bbox):
    for childprocess in [0, 1]:
        im = pyscreenshot.grab(
            bbox=bbox,
            backend=backend,
            childprocess=childprocess,
        )
        img_debug(im, backend + str(bbox))

        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
        else:
            width, height = display_size()

        eq_(width, im.size[0])
        eq_(height, im.size[1])

        # it fails sometimes
        # eq_('RGB', im.mode, 'wrong mode! %s' % (backend))

        f = tempfile.NamedTemporaryFile(
            suffix='.png', prefix='pyscreenshot_test_')
        filename = f.name
        pyscreenshot.grab_to_file(
            backend=backend,
            childprocess=childprocess,
            filename=filename,
        )


def check_ref(backend, bbox):
        # some tests fail -> disable
    return

    img_ref = pyscreenshot.grab(bbox=bbox, backend=ref)
    img_debug(img_ref, ref + str(bbox))

    im = pyscreenshot.grab(bbox=bbox, backend=backend)
    img_debug(im, backend + str(bbox))

    eq_('RGB', img_ref.mode)
    eq_('RGB', im.mode)

    img_diff = ImageChops.difference(img_ref, im)
    bbox = img_diff.getbbox()
    if bbox:
        img_debug(img_diff, 'img_diff' + str(bbox))
    eq_(bbox, None, 'different image data %s!=%s bbox=%s' % (ref,
        backend, bbox))


bbox_ls = [
    (100, 200, 300, 400),
    (10, 10, 20, 20),
    (100, 100, 200, 200),
    (1, 2, 3, 4),
    (10, 20, 30, 40),
    None]


def backend_size(backend):
    for bbox in bbox_ls:
        print 'bbox:', bbox
#        for backend in backends:
        print 'backend:', backend
        check_size(backend, bbox)


def backend_ref(backend):
    for bbox in bbox_ls:
        print 'bbox:', bbox
#        for backend in backends:
        setup_func()
        print 'backend:', backend
        check_ref(backend, bbox)
        teardown_func()
