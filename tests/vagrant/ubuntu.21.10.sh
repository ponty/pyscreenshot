#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT update
$APT dist-upgrade

$APT install ubuntu-desktop^

cd /vagrant/tests/vagrant
# ./gdm3.sh
./ubu1804dep.sh

$APT install lightdm
$APT remove sddm gdm3 gnome-keyring

# autologin
echo '
[Seat:*]
autologin-user=vagrant
autologin-session=ubuntu
' > /etc/lightdm/lightdm.conf.d/12-autologin.conf

# autostart terminal
# echo '
# exec kitty
# ' >> /etc/sway/config

