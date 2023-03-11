from bt import backend_to_check, prog_check

if prog_check(["ksnip", "--version"]):

    def test_scrot():
        backend_to_check("scrot")
