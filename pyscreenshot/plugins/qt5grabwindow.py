import io
import logging

from PIL import Image

from pyscreenshot.plugins.backend import CBackend

log = logging.getLogger(__name__)

# based on qt4 backend

app = None


class Qt5GrabWindow(CBackend):
    name = "pyqt5"

    # qt backends have conflict with each other in the same process.

    def grab_to_buffer(self, buff, file_type="png"):
        from PyQt5 import Qt, QtGui, QtWidgets  # type: ignore

        QApplication = QtWidgets.QApplication
        QBuffer = Qt.QBuffer
        QIODevice = Qt.QIODevice
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
        strio = io.BytesIO()
        self.grab_to_buffer(strio)
        strio.seek(0)
        im = Image.open(strio)
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        from PyQt5 import Qt

        return Qt.PYQT_VERSION_STR
