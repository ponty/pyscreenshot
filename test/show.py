import logging
import pyscreenshot as ImageGrab

def show():
    logging.basicConfig(level=logging.DEBUG)
    im=ImageGrab.grab(bbox=(10,10,500,500))
    im.show()
if __name__ == "__main__": show() 
