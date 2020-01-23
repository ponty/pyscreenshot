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

# based on qt5 backend


class QtPyGrabWindow(object):
    name = "qtpy"
    childprocess = False

    def __init__(self):
        import qtpy

        self.qtpy = qtpy
        from qtpy import QtGui
        from qtpy import QtCore
        from qtpy import QtWidgets

        self.app = None
        self.QtGui = QtGui
        self.QtCore = QtCore
        self.QtWidgets = QtWidgets

    def grab_to_buffer(self, buff, file_type="png"):
        QApplication = self.QtWidgets.QApplication
        QBuffer = self.qtpy.QtCore.QBuffer
        QIODevice = self.qtpy.QtCore.QIODevice
        QScreen = self.qtpy.QtGui.QScreen

        if not self.app:
            self.app = QApplication([])
        qbuffer = QBuffer()
        qbuffer.open(QIODevice.ReadWrite)
        QScreen.grabWindow(
            QApplication.primaryScreen(), QApplication.desktop().winId()
        ).save(qbuffer, file_type)
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
        return self.qtpy.__version__
