#!/bin/sh
/vagrant/tests/vagrant/ubudep.sh

export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT install kubuntu-desktop^
$APT remove sddm
$APT install lightdm

# autologin
echo '
[Seat:*]
autologin-user=vagrant
autologin-session=plasma
' >>/etc/lightdm/lightdm.conf.d/12-autologin.conf

# disable screen lock
sudo -H -u vagrant bash -c 'mkdir -p /home/vagrant/.config'
echo '[$Version]
update_info=kscreenlocker.upd:0.1-autolock

[Daemon]
Autolock=false
Timeout=60' >/home/vagrant/.config/kscreenlockerrc

# autostart konsole
sudo -H -u vagrant bash -c 'mkdir -p /home/vagrant/.config/autostart/ && cp /usr/share/applications/org.kde.konsole.desktop /home/vagrant/.config/autostart/'

# TODO: pyqt5 crash:
apt-get -y remove python3-pyqt5
