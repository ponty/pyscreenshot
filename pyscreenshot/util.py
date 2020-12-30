import os
import sys

from easyprocess import EasyProcess


def py_minor():
    return sys.version_info[1]


def platform_is_osx():
    return sys.platform == "darwin"


def platform_is_win():
    return sys.platform == "win32"


def platform_is_linux():
    return sys.platform.startswith("linux")


def use_x_display():
    if platform_is_win():
        return False
    if platform_is_osx():
        return False
    DISPLAY = os.environ.get("DISPLAY")
    XDG_SESSION_TYPE = os.environ.get("XDG_SESSION_TYPE")
    # Xwayland can not be used for screenshot
    return DISPLAY and XDG_SESSION_TYPE != "wayland"


def extract_version(txt):
    """This function tries to extract the version from the help text of any
    program."""
    words = txt.replace(",", " ").split()
    version = None
    for x in reversed(words):
        if len(x) > 2:
            if x[0].lower() == "v":
                x = x[1:]
            if "." in x and x[0].isdigit():
                version = x
                break
    return version


def run_mod_as_subproc(name, params=[]):
    python = sys.executable
    cmd = [python, "-m", name] + params
    p = EasyProcess(cmd).call()
    return p
