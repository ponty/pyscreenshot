import logging
import sys

from PIL import Image

PY2 = sys.version_info[0] == 2

if PY2:
    import StringIO

    BytesIO = StringIO.StringIO
else:
    import io

    BytesIO = io.BytesIO


log = logging.getLogger(__name__)


# based on:
# http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux


class Qt4GrabWindow(object):
    name = "pyqt"
    childprocess = False

    app = None

    def __init__(self):
        import PyQt4

        self.PyQt4 = PyQt4
        from PyQt4 import QtGui
        from PyQt4 import Qt

        self.QtGui = QtGui
        self.Qt = Qt

    def grab_to_buffer(self, buff, file_type="png"):
        QApplication = self.PyQt4.QtGui.QApplication
        QBuffer = self.PyQt4.Qt.QBuffer
        QIODevice = self.PyQt4.Qt.QIODevice
        QPixmap = self.PyQt4.QtGui.QPixmap

        if not self.__class__.app:
            self.__class__.app = QApplication([])
        qbuffer = QBuffer()
        qbuffer.open(QIODevice.ReadWrite)
        QPixmap.grabWindow(QApplication.desktop().winId()).save(qbuffer, file_type)
        buff.write(qbuffer.data())
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
        return self.PyQt4.Qt.PYQT_VERSION_STR
