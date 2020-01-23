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

# TODO:PY2 error:
#        TypeError: 'PySide2.QtGui.QScreen.grabWindow' called with wrong argument types:
#           PySide2.QtGui.QScreen.grabWindow(int)
#        Supported signatures:
#           PySide2.QtGui.QScreen.grabWindow(WId, int = 0, int = 0, int = -1, int = -1)
# https://stackoverflow.com/questions/59118938/type-error-when-calling-qscreen-grabwindow


class PySide2BugError(Exception):
    pass


class PySide2GrabWindow(object):
    name = "pyside2"
    childprocess = False

    app = None

    def __init__(self):
        if PY2:
            raise PySide2BugError()
        import PySide2

        self.PySide2 = PySide2
        from PySide2 import QtGui
        from PySide2 import QtCore
        from PySide2 import QtWidgets

        self.QtGui = QtGui
        self.QtCore = QtCore
        self.QtWidgets = QtWidgets

    def grab_to_buffer(self, buff, file_type="png"):
        QApplication = self.PySide2.QtWidgets.QApplication
        QBuffer = self.PySide2.QtCore.QBuffer
        QIODevice = self.PySide2.QtCore.QIODevice
        QScreen = self.PySide2.QtGui.QScreen
        # QPixmap = self.PySide2.QtGui.QPixmap

        if not self.__class__.app:
            self.__class__.app = QApplication([])
        qbuffer = QBuffer()
        qbuffer.open(QIODevice.ReadWrite)
        QScreen.grabWindow(
            QApplication.primaryScreen(), QApplication.desktop().winId()
        ).save(qbuffer, file_type)
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
        return self.PySide2.__version__
