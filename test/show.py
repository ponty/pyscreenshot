import logging
import pyscreenshot as ImageGrab
import time

def show():
    logging.basicConfig(level=logging.DEBUG)
    im=[]
    im.append(ImageGrab.grab(bbox=(100,200,300,400), force_backend='pygtk'))
    im.append(ImageGrab.grab(bbox=(100,200,300,400), force_backend='scrot'))
    im.append(ImageGrab.grab(bbox=(100,200,300,400), force_backend='imagemagick'))
    
    for x in im:
        x.show()
        time.sleep(1)

if __name__ == "__main__": 
    show() 
