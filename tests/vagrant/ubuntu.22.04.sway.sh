#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT update
$APT dist-upgrade

$APT install grim sway kitty


# autologin
echo '
[daemon]
AutomaticLoginEnable = true
AutomaticLogin = vagrant
' > /etc/gdm3/custom.conf


cd /vagrant/tests/vagrant
./ubu1804dep.sh

# $APT install lightdm
# $APT remove sddm gdm3 gnome-keyring

# autologin
# echo '
# [Seat:*]
# autologin-user=vagrant
# autologin-session=sway
# ' > /etc/lightdm/lightdm.conf.d/12-autologin.conf

# autostart terminal
echo '
exec kitty
' >> /etc/sway/config

