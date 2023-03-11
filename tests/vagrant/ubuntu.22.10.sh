#!/bin/sh
/vagrant/tests/vagrant/ubudep.sh

export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT install ubuntu-desktop-minimal

# autologin
echo '
[daemon]
AutomaticLoginEnable = true
AutomaticLogin = vagrant
' >/etc/gdm3/custom.conf

# autostart gnome terminal
sudo -H -u vagrant bash -c 'mkdir -p /home/vagrant/.config/autostart/ && cp /usr/share/applications/org.gnome.Terminal.desktop /home/vagrant/.config/autostart/'
