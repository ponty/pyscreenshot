# -*- coding: utf-8 -*-
"""Gdk3-based screenshotting.

Adapted from https://stackoverflow.com/a/37768950/81636, but uses
buffers directly instead of saving intermediate files (which is slow).
"""
from PIL import Image

Gdk = None
GdkPixbuf = None


class Gdk3PixbufWrapper(object):
    name = 'pygdk3'
    childprocess = False

    def __init__(self):
        global Gdk, GdkPixbuf
        import gi
        gi.require_version('Gdk', '3.0')
        from gi.repository import Gdk as _Gdk
        from gi.repository import GdkPixbuf as _GdkPixbuf
        Gdk, GdkPixbuf = _Gdk, _GdkPixbuf

    def grab(self, bbox=None):
        """Grabs an image directly to a buffer.

        :param bbox: Optional tuple or list containing (x1, y1, x2, y2) coordinates
            of sub-region to capture.
        :return: PIL RGB image
        :raises: ValueError, if image data does not have 3 bytes per pixel.
        :rtype: Image
        """
        w = Gdk.get_default_root_window()
        if bbox is not None:
            g = [bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]]
        else:
            g = w.get_geometry()
        pb = Gdk.pixbuf_get_from_window(w, *g)
        pixel_bytes = pb.read_pixel_bytes().get_data()  # type: bytes
        bytes_per_pixel = len(pixel_bytes) // (g[2] * g[3])
        if bytes_per_pixel != 3:
            raise ValueError(
                "Got {} bytes per pixel, expected 3.".format(bytes_per_pixel))
        return Image.frombytes('RGB', (g.width, g.height), pixel_bytes, 'raw')

    def grab_to_file(self, filename, bbox=None):
        self.grab(bbox=bbox).save(filename)

    def backend_version(self):
        import gi
        return '.'.join(map(str, gi.version_info))
