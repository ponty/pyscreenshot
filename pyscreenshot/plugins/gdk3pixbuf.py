# -*- coding: utf-8 -*-
"""Gdk3-based screenshotting.

Adapted from https://stackoverflow.com/a/37768950/81636, but uses
buffers directly instead of saving intermediate files (which is slow).
"""

from PIL import Image

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.util import platform_is_osx


class Gdk3BackendError(Exception):
    pass


class Gdk3PixbufWrapper(CBackend):
    name = "pygdk3"

    def grab(self, bbox=None):
        """Grabs an image directly to a buffer.

        :param bbox: Optional tuple or list containing (x1, y1, x2, y2) coordinates
            of sub-region to capture.
        :return: PIL RGB image
        :raises: ValueError, if image data does not have 3 channels (RGB), each with 8
            bits.
        :rtype: Image
        """
        if platform_is_osx():
            raise Gdk3BackendError("osx not supported")
        import gi  # type: ignore

        gi.require_version("Gdk", "3.0")
        # gi.require_version('GdkPixbuf', '2.0')
        from gi.repository import Gdk, GdkPixbuf  # type: ignore

        # read_pixel_bytes: New in version 2.32.
        if GdkPixbuf.PIXBUF_MAJOR == 2:
            if GdkPixbuf.PIXBUF_MINOR < 32:
                raise ValueError(
                    "GdkPixbuf min supported version: 2.32   current:"
                    + GdkPixbuf.PIXBUF_VERSION
                )

        w = Gdk.get_default_root_window()
        if bbox is not None:
            g = [bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]]
        else:
            g = w.get_geometry()
        pb = Gdk.pixbuf_get_from_window(w, *g)
        if not pb:
            raise Gdk3BackendError("empty buffer")

        if pb.get_bits_per_sample() != 8:
            raise Gdk3BackendError("Expected 8 bits per pixel.")
        elif pb.get_n_channels() != 3:
            raise Gdk3BackendError("Expected RGB image.")

        # Read the entire buffer into a python bytes object.
        # read_pixel_bytes: New in version 2.32.
        pixel_bytes = pb.read_pixel_bytes().get_data()  # type: bytes
        width, height = g[2], g[3]

        # Probably for SSE alignment reasons, the pixbuf has extra data in each line.
        # The args after "raw" help handle this; see
        # http://effbot.org/imagingbook/decoder.htm#the-raw-decoder
        return Image.frombytes(
            "RGB", (width, height), pixel_bytes, "raw", "RGB", pb.get_rowstride(), 1
        )

    def backend_version(self):
        import gi

        return ".".join(map(str, gi.version_info))
