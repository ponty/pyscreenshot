import atexit
import logging
import os
import shutil
import tempfile
from logging import DEBUG

log = logging.getLogger(__name__)

CLEANUP = False

# for image debug
USE_TESTOUT_DIR = 1


class ImageDebug(object):
    def __init__(self):
        self.index = 0
        d = None
        if USE_TESTOUT_DIR:
            d = os.path.join(os.getcwd(), "testout")
            os.makedirs(d, exist_ok=True)
        self.dir = tempfile.mkdtemp(dir=d, prefix="pyscreenshot_img_")
        if CLEANUP:
            atexit.register(shutil.rmtree, self.dir)

    def img_debug(self, im, text):
        if not log.isEnabledFor(DEBUG):
            return
        fname = os.path.join(self.dir, str(self.index).zfill(3) + "_" + text + ".png")
        im.save(fname)
        log.debug("image (%s) was saved:" % im + fname)
        self.index += 1
