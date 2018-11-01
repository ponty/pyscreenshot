from multiprocessing import Process, Queue
import traceback
import logging

log = logging.getLogger(__name__)


def _wrapper(target, codec, queue, args, kwargs):
    exc = tb = None
    try:
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        r = target(*args, **kwargs)
    except Exception as e:
        r = None
        exc = e
        tb = traceback.format_exc()

    if codec:
        r = codec[0](r)

    queue.put((tb, exc, r))


def run_in_childprocess(target, codec=None, *args, **kwargs):
    assert codec is None or len(codec) == 2, codec
    queue = Queue()
    p = Process(target=_wrapper, args=(target, codec, queue, args, kwargs))
    p.start()
    tb, e, r = queue.get()
    p.join()

    if e:
        log.error(tb)
        raise e

    if codec:
        r = codec[1](r)

    return r
