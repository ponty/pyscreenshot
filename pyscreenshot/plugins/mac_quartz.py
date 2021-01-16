# Javier Escalada Gomez
#
# from:
# https://stackoverflow.com/questions/4524723/take-screenshot-in-python-on-mac-os-x

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.tempexport import read_func_img


class MacQuartzWrapper(CBackend):
    name = "mac_quartz"

    def grab(self, bbox=None):

        im = read_func_img(self._grab_to_file, bbox)
        return im

    def _grab_to_file(self, filename, bbox=None, dpi=72):
        # Should query dpi from somewhere, e.g for retina displays?
        import Quartz
        import LaunchServices
        from Cocoa import NSURL
        import Quartz.CoreGraphics as CG

        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            region = CG.CGRectMake(bbox[0], bbox[1], width, height)
        else:
            region = CG.CGRectInfinite

        # Create screenshot as CGImage
        image = CG.CGWindowListCreateImage(
            region,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault,
        )

        file_type = LaunchServices.kUTTypePNG

        url = NSURL.fileURLWithPath_(filename)

        dest = Quartz.CGImageDestinationCreateWithURL(
            url,
            file_type,
            # 1 image in file
            1,
            None,
        )

        properties = {
            Quartz.kCGImagePropertyDPIWidth: dpi,
            Quartz.kCGImagePropertyDPIHeight: dpi,
        }

        # Add the image to the destination, characterizing the image with
        # the properties dictionary.
        Quartz.CGImageDestinationAddImage(dest, image, properties)

        # When all the images (only 1 in this example) are added to the destination,
        # finalize the CGImageDestination object.
        Quartz.CGImageDestinationFinalize(dest)

    def backend_version(self):
        import objc

        return objc.__version__
