import os
from time import sleep

import fabric
import vagrant
from entrypoint2 import entrypoint
from path import Path

# from fabric.api import env, execute, task, run, sudo, settings
from vncdotool import api

# pip3 install fabric vncdotool python-vagrant entrypoint2

DIR = Path(__file__).parent.parent.parent

g_nohalt = False


def box(vagrantfile, cmds):
    env = os.environ
    if vagrantfile:
        env["VAGRANT_VAGRANTFILE"] = DIR / vagrantfile
        env["VAGRANT_DOTFILE_PATH"] = DIR / ".vagrant_" + vagrantfile
    v = vagrant.Vagrant(env=env, quiet_stdout=False, quiet_stderr=False)
    if not g_nohalt:
        v.halt()  # avoid screensaver
    v.up()
    try:
        with fabric.Connection(
            v.user_hostname_port(), connect_kwargs={"key_filename": v.keyfile(),},
        ) as conn:
            with conn.cd("/vagrant"):
                conn.run("env")
                conn.run("free -h")
                # sleep(10)
                for cmd in cmds:
                    conn.run(cmd)
    finally:
        if not g_nohalt:
            v.halt()


def ubu1804(prefix=""):
    box(
        f"Vagrantfile.{prefix}ubuntu.18.04.rb",
        ["tox -e py2-desktop", "tox -e py3-desktop",],
    )


# def arch_kde(wm):
#     box(
#         f"Vagrantfile.arch.kde.{wm}.rb",
#         [
#             "tox -e py3-desktop",
#         ],
#     )


@entrypoint
def main(nohalt=False):
    global g_nohalt
    g_nohalt = nohalt
    # box(
    #     None, ["tox"],
    # )
    # ubu1804("l")
    # ubu1804("x")
    # ubu1804("k")
    # ubu1804()
    # arch_kde("x11")
    # arch_kde("wayland")
    # box("Vagrantfile.arch.kde.x11.rb", ["tox -e py3-desktop"])
    box("Vagrantfile.arch.kde.wayland.rb", ["tox -e py3-desktop-d1"])

    # box("Vagrantfile.win.rb", ["tox -e py3-desktop"])
    # box("Vagrantfile.osx.rb", ["tox -e py3-desktop"])
