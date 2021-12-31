"""
import logging
import tempfile
import tkinter
from os.path import join

from entrypoint2 import entrypoint
from PIL import Image, ImageTk

from genimg import generate_image
from pyscreenshot.util import platform_is_osx

log = logging.getLogger(__name__)


# https://stackoverflow.com/questions/47316266/can-i-display-image-in-full-screen-mode-with-pil/47317411
def fillscreen_tk(fimage):
    pilImage = Image.open(fimage)
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    root.config(cursor="none")
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    root.bind("q", lambda e: (e.widget.withdraw(), e.widget.quit()))

    # print(w,h)
    canvas = tkinter.Canvas(root, width=w, height=h)
    canvas.pack()
    canvas.configure(background="red")
    assert pilImage.size == (w, h)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w / 2, h / 2, image=image)

    # make fullscreen
    if platform_is_osx():
        root.tk.call(
            "::tk::unsupported::MacWindowStyle", "style", root._w, "plain", "none"
        )
    root.attributes("-fullscreen", True)
    # root.overrideredirect(True)
    root.attributes("-topmost", True)

    root.mainloop()


@entrypoint
def main(image=""):
    if not image:
        d = tempfile.mkdtemp(prefix="fillscreen")
        image = join(d, "ref.png")
        im = generate_image()
        im.save(image)
    fillscreen_tk(image)
"""
