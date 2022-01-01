#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef -y --allow-downgrades --allow-remove-essential --allow-change-held-packages"

sudo update-locale LANG=en_US.UTF-8 LANGUAGE=en.UTF-8
# echo 'export export LC_ALL=C' >> /home/vagrant/.profile

# install python versions
sudo add-apt-repository --yes ppa:deadsnakes/ppa
# sudo add-apt-repository --yes  ppa:jan-simon/pqiv
sudo apt-get update
sudo apt-get install -y python3.6-dev
sudo apt-get install -y python3.7-dev
sudo apt-get install -y python3.8-dev
sudo apt-get install -y python3-distutils
sudo apt-get install -y python3.9-dev
sudo apt-get install -y python3.9-distutils
sudo apt-get install -y python3.10-dev
sudo apt-get install -y python3.10-distutils

# tools
sudo apt-get install -y mc xvfb
sudo apt-get install -y python3-pip
sudo pip3 install -U pip

# for pillow source install
#  sudo apt-get install -y libjpeg-dev zlib1g-dev

# project dependencies
sudo apt-get install -y grim
sudo apt-get install -y maim
sudo apt-get install -y scrot
sudo apt-get install -y imagemagick
sudo apt-get install -y gnome-screenshot

sudo apt-get install -y libcanberra-gtk-module

sudo apt-get install -y python3-gi
sudo apt-get install -y gir1.2-gtk-3.0
sudo apt-get install -y libcanberra-gtk3-module

sudo apt-get install -y python3-wxgtk4.0

sudo apt-get install -y python3-pyqt4
sudo apt-get install -y python3-pyqt5
sudo apt-get install -y python3-pyside

#sudo apt-get install -y python3-pyside2 # no python3-pyside2 before disco (19.04)
sudo pip3 install pyside2 --no-cache-dir

# test dependencies
sudo apt-get install -y x11-utils
sudo pip3 install -U tox

# doc dependencies
sudo apt-get install -y graphviz
