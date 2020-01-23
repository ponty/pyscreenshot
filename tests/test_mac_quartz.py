from ref import backend_check


def test_mac_quartz():
    backend_check('mac_quartz', childprocess=True)
    backend_check('mac_quartz', childprocess=False)


# from ref import backend_ref
# from size import backend_size


# def test_size_mac_quartz():
#     backend_size('mac_quartz',  childprocess=True)
#     backend_size('mac_quartz',  childprocess=False)
# # test_size_mac_quartz.mac=1

# # TODO: fix test
# # def test_ref_mac_quartz():
# #     backend_ref('mac_quartz',  ref='pil',  childprocess=True)
# #     backend_ref('mac_quartz',  ref='pil',  childprocess=False)
# # test_ref_mac_quartz.mac=1
