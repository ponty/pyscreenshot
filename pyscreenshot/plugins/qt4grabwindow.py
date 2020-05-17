import logging

from PIL import Image

from pyscreenshot.plugins.backend import CBackend
from pyscreenshot.util import py2

if py2():
    import StringIO

    BytesIO = StringIO.StringIO
else:
    import io

    BytesIO = io.BytesIO


log = logging.getLogger(__name__)


# based on:
# http://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-linux

app = None


class Qt4GrabWindow(CBackend):
    name = "pyqt"

    def __init__(self):
        pass

    def grab_to_buffer(self, buff, file_type="png"):
        from PyQt4 import QtGui
        from PyQt4 import Qt

        QApplication = QtGui.QApplication
        QBuffer = Qt.QBuffer
        QIODevice = Qt.QIODevice
        QPixmap = QtGui.QPixmap

        global app
        if not app:
            app = QApplication([])
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
        from PyQt4 import Qt

        return Qt.PYQT_VERSION_STR
