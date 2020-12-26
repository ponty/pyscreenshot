#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT update
$APT dist-upgrade

$APT install grim sway

cd /vagrant/tests/vagrant
./ubu1804dep.sh

$APT install lightdm
$APT remove sddm gdm3 gnome-keyring

# autologin
echo '
[Seat:*]
autologin-user=vagrant
autologin-session=sway
' >> /etc/lightdm/lightdm.conf.d/12-autologin.conf

