from ref import backend_to_check, check_import

if check_import("qtpy"):

    def test_qtpy():
        backend_to_check("qtpy")
