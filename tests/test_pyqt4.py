from ref import backend_to_check, check_import

if check_import("PyQt4"):

    def test_pyqt4():
        backend_to_check("pyqt")
