#!/bin/sh
export DEBIAN_FRONTEND=noninteractive 
sudo apt-get update

# to avoid system message about upgrades
# sudo apt-get upgrade -y

# gnome
sudo apt-get install -y gnome-core gnome-screenshot

# test dependencies
# sudo add-apt-repository --yes  ppa:jan-simon/pqiv
# sudo apt-get update
sudo apt-get install -y pqiv x11-utils xvfb python3-pip
sudo python3 -m pip install tox

# tools
sudo apt-get install -y mc htop

# autologin
echo '
[daemon]
AutomaticLoginEnable = true
AutomaticLogin = vagrant
' > /etc/gdm3/daemon.conf

# Disable Lock Screen and Screen Saver Locking
sudo -H -u vagrant bash -c 'dbus-launch gsettings set org.gnome.desktop.session idle-delay 0'

# disable notifications
sudo -H -u vagrant bash -c 'dbus-launch gsettings set org.gnome.desktop.notifications show-banners false'

# autostart terminal
sudo -H -u vagrant bash -c 'mkdir -p /home/vagrant/.config/autostart/ && cp /usr/share/applications/org.gnome.Terminal.desktop /home/vagrant/.config/autostart/'


