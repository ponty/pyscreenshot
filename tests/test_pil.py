from ref import backend_check


def test_pil():
    backend_check("pil", childprocess=True)
    backend_check("pil", childprocess=False)


# from ref import backend_ref
# from size import backend_size


# def test_size_pil():
#     backend_size('pil', childprocess=True)
#     backend_size('pil', childprocess=False)
# # test_size_pil.mac=1

# # TODO: fix test
# # def test_ref_pil():
# #     backend_ref('pil',  ref='pil',  childprocess=True)
# #     backend_ref('pil',  ref='pil',  childprocess=False)
# # test_ref_pil.mac=1
