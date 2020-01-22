from ref import backend_check

def test_qtpy():
    backend_check('qtpy', childprocess=True)
    backend_check('qtpy', childprocess=False)
