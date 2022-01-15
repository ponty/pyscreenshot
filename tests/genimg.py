import logging

from entrypoint2 import entrypoint
from PIL import Image

# from size import display_size

log = logging.getLogger(__name__)


def generate_image(w, h):
    # w, h = display_size()
    log.debug("display size: %s x %s", w, h)
    if w <= 0 or h <= 0:
        raise ValueError("invalid display size %s x %s" % (w, h))
    img = Image.new("RGB", (w, h), "black")  # Create a new black image
    pixels = img.load()  # Create the pixel map
    i = 0
    B = 42
    for x in range(img.size[0]):  # For every pixel:
        for y in range(img.size[1]):
            r = int(x * 255 / w)
            g = int(y * 255 / h)

            b = int(((x % B) * 255 / B + (y % B) * 255 / B) / 2)
            pixels[x, y] = (r, g, b)  # Set the colour accordingly
            i += 1
    return img


@entrypoint
def main():
    im = generate_image()
    im.show()
