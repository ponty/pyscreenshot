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

# based on qt5 backend
app = None


class QtPyGrabWindow(CBackend):
    name = "qtpy"

    def __init__(self):
        pass

    def grab_to_buffer(self, buff, file_type="png"):
        from qtpy import QtGui
        from qtpy import QtCore
        from qtpy import QtWidgets

        QApplication = QtWidgets.QApplication
        QBuffer = QtCore.QBuffer
        QIODevice = QtCore.QIODevice
        QScreen = QtGui.QScreen

        global app
        if not app:
            app = QApplication([])
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
        import qtpy

        return qtpy.__version__
