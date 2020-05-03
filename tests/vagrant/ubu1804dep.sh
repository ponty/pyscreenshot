#!/bin/sh

echo 'export export LC_ALL=C' >> /home/vagrant/.profile

# test dependencies
sudo add-apt-repository --yes  ppa:jan-simon/pqiv
sudo apt-get update
sudo apt-get install -y pqiv x11-utils xvfb python3-pip
sudo python3 -m pip install tox