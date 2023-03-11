#!/usr/bin/env python3
import os
import os.path
import threading
import time
from pathlib import Path
from tempfile import TemporaryDirectory
from time import sleep

import fabric
import imagehash
import vagrant
from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from PIL import Image

KBD_RIGHT = "e0 4d e0 cd".split()
KBD_SPACE = "39 b9".split()


def vbox_send_kbd(box, kbd):
    cmd = ["VBoxManage", "controlvm", box, "keyboardputscancode"] + kbd
    EasyProcess(cmd).call()


def close_confirm_wnd(box):
    vbox_send_kbd(box, KBD_RIGHT + KBD_RIGHT + KBD_SPACE)


def vbox_screenshot(box, bbox=None):
    with TemporaryDirectory(prefix="vbox_screenshot") as tmpdirname:
        filename = os.path.join(tmpdirname, "screenshot.png")

        cmd = ["VBoxManage", "controlvm", box, "screenshotpng", filename]
        EasyProcess(cmd).call()

        im = Image.open(filename)
        if bbox:
            im = im.crop(bbox)  # (left, upper, right, lower)
        return im


# from fabric.api import env, execute, task, run, sudo, settings


# pip3 install fabric vncdotool python-vagrant entrypoint2

DIR = Path(__file__).parent


class Options:
    halt = True
    recreate = True
    destroy = False
    fast = False
    create = False


def wrapcmd(cmd, guiproc):
    if guiproc:
        # copy env vars from graphical session
        cmd2 = f"pid=`pidof {guiproc}`"
        cmd2 += ";pid=$( cut -d ' ' -f 1 <<< $pid )"
        cmd2 += ";sudo cat /proc/$pid/environ | tr '\\0' '\\n' > /tmp/environ"
        cmd2 += ";export $(cat /tmp/environ)"
        cmd = cmd2 + f"; {cmd}"
    print(f"command: {cmd}")
    return cmd


def run_box(name, options, vagrantfile, cmds, guiproc):
    env = os.environ
    env["VAGRANT_VAGRANTFILE"] = str(DIR / vagrantfile)
    env["VAGRANT_DOTFILE_PATH"] = str(DIR / (".vagrant_" + vagrantfile))

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

    if options.create:
        return

    event = threading.Event()

    auto_confirm_thread = None
    if name == "ubuntu.22.04":

        box = "pyscreenshot_" + name

        def auto_confirm():
            confirm_wnd_hash = "0000207e3e3e0000"
            bbox = (610, 120, 670, 150)
            while True:
                if event.is_set():
                    break
                img = vbox_screenshot(box, bbox)
                h = imagehash.average_hash(img)
                # print(h)
                if str(h) == confirm_wnd_hash:
                    # print("close_confirm_wnd")
                    close_confirm_wnd(box)
                time.sleep(1)

        auto_confirm_thread = threading.Thread(target=auto_confirm)

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
                    cmds = (
                        [
                            freecmd,
                            "env | sort",
                            "gnome-shell --version || true",
                            "plasmashell --version || true",
                        ]
                        + cmds
                        + [freecmd]
                    )

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

                if auto_confirm_thread:
                    auto_confirm_thread.start()

                print(f"collected commands: {cmds}")
                for cmd in cmds:
                    if options.recreate:
                        if "tox" in cmd:
                            # cmd += " -r"
                            cmd = cmd.replace("tox", "tox -r")
                    conn.run(wrapcmd(cmd, guiproc), echo=True, pty=True)
    finally:
        event.set()
        if auto_confirm_thread:
            auto_confirm_thread.join()
        if options.halt:
            v.halt()


config = {
    "ubuntu.server.22.04": (
        ["tox"],
        "",
    ),
    "lubuntu.20.04": (
        ["tox -e py3-desktop"],
        "qterminal",
    ),
    "lubuntu.22.04": (
        ["tox -e py3-desktop"],
        "qterminal",
    ),
    "lubuntu.22.10": (
        ["tox -e py3-desktop"],
        "qterminal",
    ),
    "xubuntu.20.04": (
        ["tox -e py3-desktop"],
        "xfdesktop",
    ),
    "xubuntu.22.04": (
        ["tox -e py3-desktop"],
        "xfdesktop",
    ),
    "xubuntu.22.10": (
        ["tox -e py3-desktop"],
        "xfdesktop",
    ),
    "kubuntu.20.04": (
        ["tox -e py3-desktop"],
        "konsole",
    ),
    "kubuntu.22.04": (
        ["tox -e py3-desktop-freedesktop"],
        "konsole",
    ),
    "kubuntu.22.10": (
        ["tox -e py3-desktop-freedesktop"],
        "konsole",
    ),
    "ubuntu.20.04": (
        ["tox -e py3-desktop"],
        "gnome-terminal-server",
    ),
    "ubuntu.22.04": (
        ["tox -e py3-desktop-freedesktop"],
        "gnome-terminal-server",
    ),
    "ubuntu.22.10": (
        ["tox -e py3-desktop-freedesktop"],
        "gnome-terminal-server",
    ),
    "ubuntu.22.04.sway": (
        ["tox -e py3-desktop"],
        "foot",
    ),
    # "debian11.gnome.wayland": (
    #     ["tox -e py3-desktop"],
    #     "gnome-terminal-server",
    # ),
    # "debian11.gnome.x11": (
    #     ["tox -e py3-desktop"],
    #     "gnome-terminal-server",
    # ),
    # "debian11.kde.wayland": (
    #     ["tox -e py3-desktop"],
    #     "konsole",
    # ),
    # "debian11.kde.x11": (
    #     ["tox -e py3-desktop"],
    #     "konsole",
    # ),
    # "debian10.gnome.wayland": (
    #     # ["bash -c 'tox -e py3-desktop'"],
    #     ["tox -e py3-desktop"],
    #     "gnome-terminal-server",
    # ),
    # "debian10.gnome.x11": (
    #     # ["bash -c 'tox -e py3-desktop'"],
    #     ["tox -e py3-desktop"],
    #     "gnome-terminal-server",
    # ),
    # "debian10.kde.wayland": (
    #     ["tox -e py3-desktop"],
    #     "konsole",
    # ),
    # "debian10.kde.x11": (
    #     ["tox -e py3-desktop"],
    #     "konsole",
    # ),
    # "osx.10.14": (
    #     ["bash --login -c 'python3 -m tox -e py3-osx'"],
    #     "Dock",
    # ),
    # "osx.10.15": (
    #     ["bash --login -c 'python3 -m tox -e py3-osx'"],
    #     "Dock",
    # ),
    # "win": ("Vagrantfile.win.rb", ["tox -e py3-win"], "",),
}


@entrypoint
def main(boxes="all", fast=False, destroy=False, create=False):
    options = Options()
    options.halt = not fast
    options.recreate = not fast
    options.destroy = destroy
    options.fast = fast
    options.create = create

    if boxes == "all":
        boxes = list(config.keys())
    else:
        boxes = boxes.split(",")

    for k, v in config.items():
        name = k
        vagrantfile = "Vagrantfile." + name + ".rb"
        cmds, guiproc = v[0], v[1]
        if name in boxes:
            options.win = k.startswith("win")
            options.osx = k.startswith("osx")
            print("----->")
            print("----->")
            print("-----> %s %s %s" % (name, vagrantfile, cmds))
            print("----->")
            print("----->")
            try:
                run_box(name, options, vagrantfile, cmds, guiproc)
            finally:
                print("<-----")
                print("<-----")
                print("<----- %s %s %s" % (name, vagrantfile, cmds))
                print("<-----")
                print("<-----")
