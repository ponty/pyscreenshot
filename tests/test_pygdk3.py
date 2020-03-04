from ref import backend_to_check, check_import

if check_import("gi"):

    def test_pygdk3():
        backend_to_check("pygdk3")
