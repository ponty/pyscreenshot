#!/bin/sh
/vagrant/tests/vagrant/ubudep.sh

export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"
$APT install grim sway foot

# for pygame
$APT install libsdl2-dev libfreetype-dev python3-pip
# wheel does not work
sudo pip3 install https://files.pythonhosted.org/packages/06/bf/008bcc00ebe22fcbea016f80566216c0b8e2cfea2bfdbf72664f676069b5/pygame-2.2.0.tar.gz

# autologin
mkdir -p /etc/systemd/system/getty@tty1.service.d
echo '
[Service]
ExecStart=
ExecStart=-/sbin/agetty --noissue --autologin vagrant %I $TERM
Type=idle
' > /etc/systemd/system/getty@tty1.service.d/override.conf

# sway autostart
echo '
if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
  exec sway
fi
' > /home/vagrant/.bash_profile

# autostart terminal
echo '
exec foot
' >>/etc/sway/config
