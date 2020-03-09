#!/bin/sh

pacman -Syu  --noconfirm

# kde
pacman --needed -S --noconfirm xorg-server plasma-meta plasma-wayland-session sddm

# pqiv
pacman --needed -S --noconfirm git base-devel
sudo -u vagrant sh -c 'cd /tmp && git clone https://aur.archlinux.org/pqiv.git && cd pqiv && makepkg -si --noconfirm'

# tools
pacman --needed -S --noconfirm python-pip xorg-server-xvfb mc xorg-xdpyinfo
pip install tox

chmod a-x /usr/lib/kscreenlocker_greet

systemctl  enable sddm
systemctl  start sddm
