#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install -y kubuntu-desktop^
sudo apt-get remove -y sddm

./gdm3.sh
./ubu1804dep.sh
