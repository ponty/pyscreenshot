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
        #gi.require_version('GdkPixbuf', '2.0')
        from gi.repository import Gdk as _Gdk
        from gi.repository import GdkPixbuf as _GdkPixbuf

        # read_pixel_bytes: New in version 2.32.
        if _GdkPixbuf.PIXBUF_MAJOR == 2:
            if _GdkPixbuf.PIXBUF_MINOR < 32:
                raise ValueError(
                    'GdkPixbuf min supported version: 2.32   current:' + _GdkPixbuf.PIXBUF_VERSION)

        Gdk, GdkPixbuf = _Gdk, _GdkPixbuf

    def grab(self, bbox=None):
        """Grabs an image directly to a buffer.

        :param bbox: Optional tuple or list containing (x1, y1, x2, y2) coordinates
            of sub-region to capture.
        :return: PIL RGB image
        :raises: ValueError, if image data does not have 3 channels (RGB), each with 8
            bits.
        :rtype: Image
        """
        w = Gdk.get_default_root_window()
        if bbox is not None:
            g = [bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]]
        else:
            g = w.get_geometry()
        pb = Gdk.pixbuf_get_from_window(w, *g)
        if pb.get_bits_per_sample() != 8:
            raise ValueError('Expected 8 bits per pixel.')
        elif pb.get_n_channels() != 3:
            raise ValueError('Expected RGB image.')

        # Read the entire buffer into a python bytes object.
        # read_pixel_bytes: New in version 2.32.
        pixel_bytes = pb.read_pixel_bytes().get_data()  # type: bytes
        width, height = g[2], g[3]

        # Probably for SSE alignment reasons, the pixbuf has extra data in each line.
        # The args after "raw" help handle this; see
        # http://effbot.org/imagingbook/decoder.htm#the-raw-decoder
        return Image.frombytes(
            'RGB', (width, height), pixel_bytes, 'raw', 'RGB', pb.get_rowstride(), 1)

    def grab_to_file(self, filename, bbox=None):
        self.grab(bbox=bbox).save(filename)

    def backend_version(self):
        import gi
        return '.'.join(map(str, gi.version_info))
