UNKNOWN_VERSION = "?.?"

# qt backends have conflict with each other in the same process.
# qt is not a first choice so they are put in subprocess for isolation.
qt_apply_childprocess = True


class CBackend(object):
    is_subprocess = False
    apply_childprocess = False
