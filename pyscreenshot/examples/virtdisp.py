"Create screenshot of xmessage with Xvfb"
from time import sleep

from easyprocess import EasyProcess
from pyvirtualdisplay import Display

import pyscreenshot as ImageGrab

with Display(size=(100, 60)) as disp:  # start Xvfb display
    # display is available
    with EasyProcess(["xmessage", "hello"]):  # start xmessage
        sleep(1)  # wait for displaying window
        img = ImageGrab.grab()
img.save("xmessage.png")
