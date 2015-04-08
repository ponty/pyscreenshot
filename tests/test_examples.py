from pyvirtualdisplay.display import Display

from pyscreenshot.procutil import run_in_childprocess


def showgrabbox_subprocess():
        from pyscreenshot.examples import showgrabbox
        print(showgrabbox)

def test_showgrabbox():
    with Display(visible=0, size=(800, 600)):
        run_in_childprocess(target=showgrabbox_subprocess)
        


def showgrabfullscreen_subprocess():
        from pyscreenshot.examples import showgrabfullscreen
        print(showgrabfullscreen)

def test_showgrabfullscreen():
    with Display(visible=0, size=(800, 600)):
        run_in_childprocess(target=showgrabfullscreen_subprocess)
