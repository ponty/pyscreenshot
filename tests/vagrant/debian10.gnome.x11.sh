#!/bin/sh
cd /vagrant/tests/vagrant
./debian10.gnome.wayland.sh

echo '
WaylandEnable=false
' >> /etc/gdm3/daemon.conf