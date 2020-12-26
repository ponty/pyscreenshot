#!/bin/sh
mkdir /etc/sddm.conf.d
echo '[Autologin]
User=vagrant
Session=plasma.desktop
#Session=plasmawayland.desktop' > /etc/sddm.conf.d/autologin.conf

cd /vagrant/tests/vagrant
./debian10_kde.sh

