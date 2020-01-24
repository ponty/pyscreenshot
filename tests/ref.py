import logging
import sys

import pyscreenshot
from nose.tools import eq_
from PIL import Image, ImageChops

import fillscreen
from config import bbox_ls
from image_debug import img_debug
from size import backend_size


def check_ref(backend, bbox, childprocess):
    img_ref = Image.open("/tmp/fillscreen.bmp")
    if bbox:
        img_ref = img_ref.crop(bbox)

    im = pyscreenshot.grab(bbox=bbox, backend=backend, childprocess=childprocess)

    img_ref = img_ref.convert("RGB")
    im = im.convert("RGB")

    eq_("RGB", img_ref.mode)
    eq_("RGB", im.mode)

    img_debug(img_ref, "ref" + str(bbox))
    img_debug(im, str(backend) + str(bbox))

    img_diff = ImageChops.difference(img_ref, im)
    ex = img_diff.getextrema()
    logging.debug("diff getextrema: %s", ex)
    diff_bbox = img_diff.getbbox()
    if diff_bbox:
        img_debug(img_diff, "img_diff" + str(diff_bbox))
    eq_(
        diff_bbox,
        None,
        "different image data %s bbox=%s extrema:%s diff_bbox=%s"
        % (backend, bbox, ex, diff_bbox),
    )


def backend_ref(backend, childprocess=True):
    for bbox in bbox_ls:
        print("bbox: {}".format(bbox))
        print("backend: %s" % backend)
        check_ref(backend, bbox, childprocess)


def _backend_check(backend, childprocess):
    enable_ref = True
    if sys.platform == "darwin":
        enable_ref = False  # TODO
    if enable_ref:
        backend_ref(
            backend, childprocess=childprocess,
        )
    else:
        backend_size(
            backend, childprocess=childprocess,
        )


def backend_to_check(backend):
    fillscreen.init()
    _backend_check(backend, childprocess=True)
    # _backend_check(backend, childprocess=False) # TODO: test childprocess=False
