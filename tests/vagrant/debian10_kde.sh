#!/bin/sh
export DEBIAN_FRONTEND=noninteractive 

sudo apt-get update
# sudo apt-get upgrade -y

# kde
sudo apt-get install -y kde-plasma-desktop 

# test dependencies
# sudo add-apt-repository --yes  ppa:jan-simon/pqiv
# sudo apt-get update
sudo apt-get install -y x11-utils xvfb python3-pip 
sudo python3 -m pip install tox

# tools
sudo apt-get install -y mc htop

# TODO: pyqt5 crash:
#    $ python3 -c 'from PyQt5 import QtWidgets;app = QtWidgets.QApplication([])'
#    malloc_consolidate(): invalid chunk size
#    KCrash: crashing... crashRecursionCounter = 2
#    KCrash: Application Name = python3.7 path = /usr/bin pid = 1840
#    KCrash: Arguments: 
#    Alarm clock
# -> remove pyqt5
sudo apt-get -y remove python3-pyqt5

# disable screen lock
sudo -H -u vagrant bash -c 'mkdir -p /home/vagrant/.config'
echo '[$Version]
update_info=kscreenlocker.upd:0.1-autolock

[Daemon]
Autolock=false
Timeout=60' > /home/vagrant/.config/kscreenlockerrc

# autostart konsole
sudo -H -u vagrant bash -c 'mkdir -p /home/vagrant/.config/autostart/ && cp /usr/share/applications/org.kde.konsole.desktop /home/vagrant/.config/autostart/'
