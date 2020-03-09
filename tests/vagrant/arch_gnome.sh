#!/bin/sh

pacman -Syu  --noconfirm

# pacman --needed -S --noconfirm xorg-server 
# gnome
pacman --needed -S --noconfirm gnome gdm

# pqiv
pacman --needed -S --noconfirm git base-devel
sudo -u vagrant sh -c 'cd /tmp && git clone https://aur.archlinux.org/pqiv.git && cd pqiv && makepkg -si --noconfirm'

# tools
pacman --needed -S --noconfirm python-pip xorg-server-xvfb mc xorg-xdpyinfo
pip install tox

# autologin
echo '
[daemon]
AutomaticLoginEnable = true
AutomaticLogin = vagrant
' > /etc/gdm/custom.conf

sudo systemctl start gdm



