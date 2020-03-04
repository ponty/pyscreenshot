from ref import backend_to_check, check_import

if check_import("PyQt5"):

    def test_pyqt5():
        backend_to_check("pyqt5")
