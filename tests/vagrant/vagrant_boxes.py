#!/usr/bin/env python3
import os
from os.path import dirname, join
from time import sleep

import fabric
import vagrant
from entrypoint2 import entrypoint

# from fabric.api import env, execute, task, run, sudo, settings


# pip3 install fabric vncdotool python-vagrant entrypoint2

DIR = dirname(dirname(dirname(__file__)))


class Options:
    halt = True
    recreate = True
    destroy = False
    fast = False


def wrapcmd(cmd, guiproc):
    if guiproc:
        # copy env vars from graphical session
        cmd = f"sudo cat /proc/`pidof {guiproc}`/environ | tr '\\0' '\\n' > /tmp/x;export $(cat /tmp/x); {cmd}"
    print(f"command: {cmd}")
    return cmd


def run_box(options, vagrantfile, cmds, guiproc):
    env = os.environ
    env["VAGRANT_VAGRANTFILE"] = join(DIR, vagrantfile)
    if vagrantfile != "Vagrantfile":
        env["VAGRANT_DOTFILE_PATH"] = join(DIR, ".vagrant_" + vagrantfile)
    else:
        env["VAGRANT_DOTFILE_PATH"] = ""

    v = vagrant.Vagrant(env=env, quiet_stdout=False, quiet_stderr=False)
    status = v.status()
    state = status[0].state
    print(status)

    if options.destroy:
        v.destroy()
        return

    if options.halt:
        v.halt()  # avoid screensaver

    if state == "not_created":
        # install programs in box
        v.up()

        # restart box
        v.halt()

        if not options.fast:
            # go over first boot messages, tasks
            v.up()
            sleep(3 * 60)
            v.halt()

    try:
        v.up()

        with fabric.Connection(
            v.user_hostname_port(),
            connect_kwargs={
                "key_filename": v.keyfile(),
            },
        ) as conn:
            with conn.cd("c:/vagrant" if options.win else "/vagrant"):
                if not options.win:
                    if options.osx:
                        freecmd = "top -l 1 -s 0 | grep PhysMem"
                    else:  # linux
                        freecmd = "free -h"
                    cmds = [freecmd, "env | sort"] + cmds + [freecmd]

                if guiproc:
                    pid = None
                    while not pid:
                        print(f"waiting for {guiproc}")
                        cmd = f"bash --login -c 'pidof {guiproc} || true'"
                        print(cmd)
                        pid = conn.run(cmd).stdout
                        sleep(1)
                    print(f"{guiproc} pid={pid}")
                sleep(5)
                print(f"collected commands: {cmds}")
                for cmd in cmds:
                    if options.recreate:
                        if "tox" in cmd:
                            # cmd += " -r"
                            cmd = cmd.replace("tox", "tox -r")
                    conn.run(wrapcmd(cmd, guiproc), echo=True, pty=True)
    finally:
        if options.halt:
            v.halt()


config = {
    "server": (
        "Vagrantfile",
        ["tox"],
        "",
    ),
    "debian11.gnome.wayland": (
        "Vagrantfile.debian11.gnome.wayland.rb",
        ["tox -e py3-desktop"],
        "gnome-terminal-server",
    ),
    "debian11.gnome.x11": (
        "Vagrantfile.debian11.gnome.x11.rb",
        ["tox -e py3-desktop"],
        "gnome-terminal-server",
    ),
    # "debian11.kde.wayland": (
    #     "Vagrantfile.debian11.kde.wayland.rb",
    #     ["tox -e py3-desktop"],
    #     "konsole",
    # ),
    # "debian11.kde.x11": (
    #     "Vagrantfile.debian11.kde.x11.rb",
    #     ["tox -e py3-desktop"],
    #     "konsole",
    # ),
    "debian10.gnome.wayland": (
        "Vagrantfile.debian10.gnome.wayland.rb",
        # ["bash -c 'tox -e py3-desktop'"],
        ["tox -e py3-desktop"],
        "gnome-terminal-server",
    ),
    "debian10.gnome.x11": (
        "Vagrantfile.debian10.gnome.x11.rb",
        # ["bash -c 'tox -e py3-desktop'"],
        ["tox -e py3-desktop"],
        "gnome-terminal-server",
    ),
    "debian10.kde.wayland": (
        "Vagrantfile.debian10.kde.wayland.rb",
        ["tox -e py3-desktop"],
        "konsole",
    ),
    "debian10.kde.x11": (
        "Vagrantfile.debian10.kde.x11.rb",
        ["tox -e py3-desktop"],
        "konsole",
    ),
    # "lubuntu.18.04": (
    #     "Vagrantfile.lubuntu.18.04.rb",
    #     ["tox -e py3-desktop"],
    #     "lxsession",
    # ),
    "lubuntu.20.04": (
        "Vagrantfile.lubuntu.20.04.rb",
        ["tox -e py3-desktop"],
        "qterminal",
    ),
    # "xubuntu.18.04": (
    #     "Vagrantfile.xubuntu.18.04.rb",
    #     ["tox -e py3-desktop"],
    #     "xfdesktop",
    # ),
    "xubuntu.20.04": (
        "Vagrantfile.xubuntu.20.04.rb",
        ["tox -e py3-desktop"],
        "xfdesktop",
    ),
    # "kubuntu.18.04": (
    #     "Vagrantfile.kubuntu.18.04.rb",
    #     ["tox -e py3-desktop"],
    #     "gnome-shell",
    # ),
    "kubuntu.20.04": (
        "Vagrantfile.kubuntu.20.04.rb",
        ["tox -e py3-desktop"],
        "konsole",
    ),
    # "ubuntu.18.04": (
    #     "Vagrantfile.ubuntu.18.04.rb",
    #     ["tox -e py3-desktop"],
    #     "gnome-shell",
    # ),
    "ubuntu.20.04": (
        "Vagrantfile.ubuntu.20.04.rb",
        ["tox -e py3-desktop"],
        "gnome-shell",
    ),
    # "arch.kde.x11": (
    #     "Vagrantfile.arch.kde.x11.rb",
    #     ["tox -e py3-desktop"],
    #     "plasmashell",
    #     # "plasma_session",
    # ),
    # "arch.kde.wayland": (
    #     "Vagrantfile.arch.kde.wayland.rb",
    #     ["tox -e py3-desktop"],
    #     "plasma_session",
    #     # "Xwayland",
    # ),
    # "arch.gnome.wayland": (
    #     "Vagrantfile.arch.gnome.wayland.rb",
    #     ["tox -e py3-desktop"],
    #     "gnome-shell-calendar-server",
    #     # "Xwayland",
    # ),
    # "win": ("Vagrantfile.win.rb", ["tox -e py3-win"], "",),
    "ubuntu.21.10.sway": (
        "Vagrantfile.ubuntu.21.10.sway.rb",
        ["tox -e py3-desktop"],
        "kitty",
    ),
    # "osx.10.14": (
    #     "Vagrantfile.osx.10.14.rb",
    #     ["bash --login -c 'python3 -m tox -e py3-osx'"],
    #     "Dock",
    # ),
    "osx.10.15": (
        "Vagrantfile.osx.10.15.rb",
        ["bash --login -c 'python3 -m tox -e py3-osx'"],
        "Dock",
    ),
}


@entrypoint
def main(boxes="all", fast=False, destroy=False):
    options = Options()
    options.halt = not fast
    options.recreate = not fast
    options.destroy = destroy
    options.fast = fast

    if boxes == "all":
        boxes = list(config.keys())
    else:
        boxes = boxes.split(",")

    for k, v in config.items():
        name = k
        vagrantfile, cmds, guiproc = v[0], v[1], v[2]
        if name in boxes:
            options.win = k.startswith("win")
            options.osx = k.startswith("osx")
            print("----->")
            print("----->")
            print("-----> %s %s %s" % (name, vagrantfile, cmds))
            print("----->")
            print("----->")
            try:
                run_box(options, vagrantfile, cmds, guiproc)
            finally:
                print("<-----")
                print("<-----")
                print("<----- %s %s %s" % (name, vagrantfile, cmds))
                print("<-----")
                print("<-----")
