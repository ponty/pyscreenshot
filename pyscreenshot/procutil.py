from multiprocessing import Queue
from threading import Thread
from queue import Empty
# import traceback


def _wrapper(target, codec, queue, args, kwargs):
    exc = None
    try:
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        r = target(*args, **kwargs)
    except Exception as e:
#         traceback.print_exc()
        r = None
        exc = e

    if codec:
        r = codec[0](r)

    queue.put((exc, r))


def run_in_childprocess(target, codec=None, *args, **kwargs):
    assert codec is None or len(codec) == 2, codec
    queue = Queue()
    p = Thread(target=_wrapper, args=(target, codec, queue,  args, kwargs))
    p.start()
    try:
        e, r = queue.get(timeout=kwargs.get('timeout',20)) # the default timeout is 20 seconds
    except Empty as exp:
        raise Exception("The Screenshot child process queue was empty, Looks like the childprocess queue got blocked on something. the error is {}\n".format(str(exp)))
    p.join()

    if e:
        raise e

    if codec:
        r = codec[1](r)

    return r
