#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT update
$APT dist-upgrade

$APT install xubuntu-desktop^

cd /vagrant/tests/vagrant
./lightdm.sh
./ubu1804dep.sh
