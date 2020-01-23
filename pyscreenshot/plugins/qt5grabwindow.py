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

# based on qt4 backend


class Qt5GrabWindow(object):
    name = "pyqt5"
    childprocess = False

    app = None

    def __init__(self):
        import PyQt5

        self.PyQt5 = PyQt5
        from PyQt5 import QtGui
        from PyQt5 import Qt
        from PyQt5 import QtWidgets

        self.QtGui = QtGui
        self.Qt = Qt
        self.QtWidgets = QtWidgets

    def grab_to_buffer(self, buff, file_type="png"):
        QApplication = self.QtWidgets.QApplication
        QBuffer = self.PyQt5.Qt.QBuffer
        QIODevice = self.PyQt5.Qt.QIODevice
        QScreen = self.PyQt5.QtGui.QScreen

        if not self.__class__.app:
            self.__class__.app = QApplication([])
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
        return self.Qt.PYQT_VERSION_STR
