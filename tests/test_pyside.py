from ref import backend_to_check, check_import


if check_import("PySide"):
    def test_pyside():
        backend_to_check("pyside")

