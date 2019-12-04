from PIL import Image
import logging
import sys
PY3 = sys.version_info[0] >= 3

if PY3:
    import io
    BytesIO = io.BytesIO
else:
    import StringIO
    BytesIO = StringIO.StringIO


log = logging.getLogger(__name__)

# based on qt4 backend


class PySideGrabWindow(object):
    name = 'pyside'
    childprocess = False

    def __init__(self):
        import PySide
        self.PySide = PySide
        from PySide import QtGui
        from PySide import QtCore
        self.app = None
        self.QtGui = QtGui
        self.QtCore = QtCore

    def grab_to_buffer(self, buff, file_type='png'):
        QApplication = self.PySide.QtGui.QApplication
        QBuffer = self.PySide.QtCore.QBuffer
        QIODevice = self.PySide.QtCore.QIODevice
        QPixmap = self.PySide.QtGui.QPixmap

        if not self.app:
            self.app = QApplication([])
        qbuffer = QBuffer()
        qbuffer.open(QIODevice.ReadWrite)
        QPixmap.grabWindow(
            QApplication.desktop().winId()).save(qbuffer, file_type)
        # https://stackoverflow.com/questions/52291585/pyside2-typeerror-bytes-object-cannot-be-interpreted-as-an-integer
        buff.write(qbuffer.data().data())
        qbuffer.close()

    def grab(self, bbox=None):
        strio = BytesIO()
        self.grab_to_buffer(strio)
        strio.seek(0)
        im = Image.open(strio)
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return self.PySide.__version__
