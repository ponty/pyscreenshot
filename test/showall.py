from pyscreenshot.backendloader import BackendLoader
import logging
import pyscreenshot as ImageGrab
import time

def show():
    logging.basicConfig(level=logging.DEBUG)
    im=[]
    
    man=BackendLoader()
    man.force('scrot')
    im.append(ImageGrab.grab(bbox=(100,200,300,400)))
    
    man.force('pygtk')
    im.append(ImageGrab.grab(bbox=(100,200,300,400)))
    
    man.force('imagemagick')
    im.append(ImageGrab.grab(bbox=(100,200,300,400)))
    
    for x in im:
        x.show()
        time.sleep(1)

if __name__ == "__main__": 
    show() 
