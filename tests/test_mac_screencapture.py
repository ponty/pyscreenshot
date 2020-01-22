from ref import backend_check




def test_mac_screencapture():
    backend_check('mac_screencapture', childprocess=True)
    backend_check('mac_screencapture', childprocess=False)

# from ref import backend_ref
# from size import backend_size


# def test_size_mac_screencapture():
#     backend_size('mac_screencapture')
#     backend_size('mac_screencapture')
# # test_size_mac_screencapture.mac=1

# def test_ref_mac_screencapture():
#     backend_ref('mac_screencapture',  ref='pil')
#     backend_ref('mac_screencapture',  ref='pil')
# # test_ref_mac_screencapture.mac=1
