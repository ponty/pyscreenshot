from pyscreenshot import grab
import logging

def show():
    logging.basicConfig(level=logging.DEBUG)
    im = grab(bbox=(100, 200, 300, 400))
    im.show()

if __name__ == "__main__": 
    show() 
