#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT update
$APT dist-upgrade

$APT install ubuntu-desktop-minimal

# autologin
echo '
[daemon]
AutomaticLoginEnable = true
AutomaticLogin = vagrant
' > /etc/gdm3/custom.conf


cd /vagrant/tests/vagrant
# ./gdm3.sh
./ubu1804dep.sh
