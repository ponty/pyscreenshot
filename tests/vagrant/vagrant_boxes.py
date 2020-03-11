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


class Options:
    halt = True
    recreate = True
    destroy = False


def wrapcmd(cmd, guiproc):
    # TODO

    if guiproc:
        # copy env vars from graphical session
        cmd = f"sudo cat /proc/`pidof {guiproc}`/environ | tr '\\0' '\\n' > /tmp/x;export $(cat /tmp/x); {cmd}"
    print(f"command: {cmd}")
    return cmd


def run_box(options, vagrantfile, cmds, guiproc):
    env = os.environ
    env["VAGRANT_VAGRANTFILE"] = DIR / vagrantfile
    env["VAGRANT_DOTFILE_PATH"] = DIR / ".vagrant_" + vagrantfile
    v = vagrant.Vagrant(env=env, quiet_stdout=False, quiet_stderr=False)
    if options.destroy:
        v.destroy()
        return
    if options.halt:
        v.halt()  # avoid screensaver

    try:
        v.up()

        with fabric.Connection(
            v.user_hostname_port(), connect_kwargs={"key_filename": v.keyfile(),},
        ) as conn:
            with conn.cd("/vagrant"):
                cmds = ["free -h", "env | sort"] + cmds
                if guiproc:
                    pid = None
                    while not pid:
                        print(f"waiting for {guiproc}")
                        pid = conn.run(f"pidof {guiproc} || true").stdout
                        sleep(1)
                    print(f"{guiproc} pid={pid}")
                sleep(1)
                for cmd in cmds:
                    if options.recreate:
                        if "tox" in cmd:
                            cmd += " -r"
                    conn.run(wrapcmd(cmd, guiproc))
    finally:
        if options.halt:
            v.halt()


config = {
    "server": ("Vagrantfile", ["tox"], "",),
    "lubuntu": (
        "Vagrantfile.lubuntu.18.04.rb",
        ["tox -e py27-desktop", "tox -e py3-desktop"],
        "lxsession",
    ),
    "xubuntu": (
        "Vagrantfile.xubuntu.18.04.rb",
        ["tox -e py27-desktop", "tox -e py3-desktop"],
        "xfdesktop",
    ),
    # TODO: fix kubuntu
    # "kubuntu": (
    #     "Vagrantfile.kubuntu.18.04.rb",
    #     ["tox -e py27-desktop", "tox -e py3-desktop"],
    #     "gnome-shell",
    # ),
    "ubuntu": ("Vagrantfile.ubuntu.18.04.rb", ["tox -e py3-desktop"], "gnome-shell",),
    "arch.kde.x11": (
        "Vagrantfile.arch.kde.x11.rb",
        ["tox -e py3-desktop"],
        "plasma_session",
    ),
    "arch.kde.wayland": (
        "Vagrantfile.arch.kde.wayland.rb",
        ["tox -e py3-desktop"],
        "plasma_session",
        # "Xwayland",
    ),
    "arch.gnome.wayland": (
        "Vagrantfile.arch.gnome.wayland.rb",
        ["tox -e py3-desktop"],
        "Xwayland",
    ),
    # "win": ("Vagrantfile.win.rb", ["tox -e py3-desktop"]),
    # "osx": ("Vagrantfile.osx.rb", ["tox -e py3-desktop"]),
    # TODO: ubuntu 20.20
}


@entrypoint
def main(boxes="all", fast=False, destroy=False):
    options = Options()
    options.halt = not fast
    options.recreate = not fast
    options.destroy = destroy

    if boxes == "all":
        boxes = list(config.keys())
    else:
        boxes = boxes.split(",")
    for k, v in config.items():
        if k in boxes:
            print("-----> %s %s %s" % (k, v[0], v[1]))
            run_box(options, v[0], v[1], v[2])

