#!/bin/sh
/vagrant/tests/vagrant/ubudep.sh

export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

$APT install xubuntu-desktop^

/vagrant/tests/vagrant/lightdm.sh
