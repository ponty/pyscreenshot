import logging
import sys


log = logging.getLogger(__name__)


def is_inside_idle():
    """True if program was started inside IDLE.

    The implementation is a HACK, because there is no correct solution.
    """
    idle = 'idlelib.run' in sys.modules
    if idle:
        log.debug('Running IDLE')
    return idle
