import logging

from easyprocess import EasyProcess

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import RunProgError, read_func_img
from pyscreenshot.util import extract_version

log = logging.getLogger(__name__)


PROGRAM = "xwd"

# wikipedia:  https://en.wikipedia.org/wiki/Xwd
#       xwd | xwdtopnm | pnmtopng > Screenshot.png
# xwdtopnm is buggy:  https://bugs.launchpad.net/ubuntu/+source/netpbm-free/+bug/1379480
# solution : imagemagick convert
#       xwd -root -display :0 | convert xwd:- file.png
# TODO: xwd sometimes grabs the wrong window so this backend will be not added now
def read_xwd_img():
    def run_prog(fpng, bbox=None):
        fxwd = fpng + ".xwd"
        pxwd = EasyProcess([PROGRAM, "-root", "-out", fxwd])
        pxwd.call()
        if pxwd.return_code != 0:
            raise RunProgError(pxwd.stderr)

        pconvert = EasyProcess(["convert", "xwd:" + fxwd, fpng])
        pconvert.call()
        if pconvert.return_code != 0:
            raise RunProgError(pconvert.stderr)

    im = read_func_img(run_prog)
    return im


class XwdWrapper(CBackend):
    name = "xwd"
    is_subprocess = True

    def grab(self, bbox=None):
        im = read_xwd_img()
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return extract_version(EasyProcess([PROGRAM, "-version"]).call().stdout)
