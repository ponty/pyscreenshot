# Javier Escalada Gomez
#
# from:
# https://stackoverflow.com/questions/4524723/take-screenshot-in-python-on-mac-os-x

from pyscreenshot.tempexport import read_func_img


class MacQuartzWrapper(object):
    name = "mac_quartz"
    childprocess = False

    def __init__(self):
        import Quartz
        import LaunchServices
        from Cocoa import NSURL
        import Quartz.CoreGraphics as CG
        import objc

        self.Quartz = Quartz
        self.LaunchServices = LaunchServices
        self.NSURL = NSURL
        self.CG = CG
        self.objc = objc

    def grab(self, bbox=None):
        im = read_func_img(self._grab_to_file, bbox)
        return im

    def _grab_to_file(self, filename, bbox=None, dpi=72):
        # FIXME: Should query dpi from somewhere, e.g for retina displays

        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            region = self.CG.CGRectMake(bbox[0], bbox[1], width, height)
        else:
            region = self.CG.CGRectInfinite

        # Create screenshot as CGImage
        image = self.CG.CGWindowListCreateImage(
            region,
            self.CG.kCGWindowListOptionOnScreenOnly,
            self.CG.kCGNullWindowID,
            self.CG.kCGWindowImageDefault,
        )

        # XXX: Can add more types:
        # https://developer.apple.com/library/mac/documentation/MobileCoreServices/Reference/UTTypeRef/Reference/reference.html#//apple_ref/doc/uid/TP40008771
        file_type = self.LaunchServices.kUTTypePNG

        url = self.NSURL.fileURLWithPath_(filename)

        dest = self.Quartz.CGImageDestinationCreateWithURL(
            url,
            file_type,
            # 1 image in file
            1,
            None,
        )

        properties = {
            self.Quartz.kCGImagePropertyDPIWidth: dpi,
            self.Quartz.kCGImagePropertyDPIHeight: dpi,
        }

        # Add the image to the destination, characterizing the image with
        # the properties dictionary.
        self.Quartz.CGImageDestinationAddImage(dest, image, properties)

        # When all the images (only 1 in this example) are added to the destination,
        # finalize the CGImageDestination object.
        self.Quartz.CGImageDestinationFinalize(dest)

    def backend_version(self):
        return self.objc.__version__
