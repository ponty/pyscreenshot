from pyvirtualdisplay.display import Display
from multiprocessing import Process, Queue

def showgrabbox_subprocess(queue):
    e=None
    try:
        from pyscreenshot.examples import showgrabbox
        print(showgrabbox)
    except Exception as e:
        pass
    queue.put(e)

def test_showgrabbox():
    with Display(visible=0, size=(800, 600)):
        queue = Queue()
        p = Process(target=showgrabbox_subprocess, args=(queue, ))
        p.start()
        e = queue.get()
        p.join()
        if e:
            raise e
    
        

def showgrabfullscreen_subprocess(queue):
    e=None
    try:
        from pyscreenshot.examples import showgrabfullscreen
        print(showgrabfullscreen)
    except Exception as e:
        pass
    queue.put(e)

def test_showgrabfullscreen():
    with Display(visible=0, size=(800, 600)):
        queue = Queue()
        p = Process(target=showgrabfullscreen_subprocess, args=(queue, ))
        p.start()
        e = queue.get()
        p.join()
        if e:
            raise e
    
