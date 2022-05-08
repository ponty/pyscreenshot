#!/bin/sh

mkdir /etc/sddm.conf.d
echo '[Autologin]
User=vagrant
#Session=plasma.desktop
Session=plasmawayland.desktop' >/etc/sddm.conf.d/autologin.conf

cd /vagrant/tests/vagrant
./debian10_kde.sh
sudo apt-get install -y plasma-workspace-wayland

sudo apt-get install -y ksnip
