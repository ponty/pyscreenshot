import atexit
import logging
import os
import shutil
import tempfile
from logging import DEBUG

log = logging.getLogger(__name__)

CLEANUP = True


class ImageDebug(object):
    def __init__(self):
        self.index = 0
        self.dir = tempfile.mkdtemp(prefix="pyscreenshot_img_")
        if CLEANUP:
            atexit.register(shutil.rmtree, self.dir)

    def img_debug(self, im, text):
        if not log.isEnabledFor(DEBUG):
            return
        fname = os.path.join(self.dir, str(self.index).zfill(3) + "_" + text + ".png")
        im.save(fname)
        log.debug("image (%s) was saved:" % im + fname)
        self.index += 1
