from pyscreenshot.examples import show, showall
from pyvirtualdisplay.display import Display


def test_show():
    with Display(visible=0, size=(800, 600)):
        show.show()


def test_showall():
    with Display(visible=0, size=(800, 600)):
        showall.show()
