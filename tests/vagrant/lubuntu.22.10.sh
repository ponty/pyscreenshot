#!/bin/sh
/vagrant/tests/vagrant/ubudep.sh

export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT install lubuntu-desktop
$APT remove sddm gdm3
$APT install lightdm

# autologin
echo '
[Seat:*]
autologin-user=vagrant
autologin-session=Lubuntu
' >>/etc/lightdm/lightdm.conf.d/12-autologin.conf

# autostart qterminal
sudo -H -u vagrant bash -c 'mkdir -p /home/vagrant/.config/autostart/ && cp /usr/share/applications/qterminal.desktop /home/vagrant/.config/autostart/'
