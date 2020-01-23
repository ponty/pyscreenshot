import logging
import os
from logging import DEBUG
from tempfile import gettempdir, mkdtemp

log = logging.getLogger(__name__)

img_dir = None
img_ind = 0


def img_debug(im, text):
    if not log.isEnabledFor(DEBUG):
        return
    global img_dir
    global img_ind
    if not img_dir:
        root = gettempdir() + "/img_debug"
        if not os.path.exists(root):
            os.makedirs(root)
        img_dir = mkdtemp(prefix="img_debug_", suffix="", dir=root)
    fname = img_dir + "/" + str(img_ind).zfill(3) + "_" + text + ".png"
    im.save(fname)
    log.debug("image (%s) was saved:" % im + fname)
    img_ind += 1
