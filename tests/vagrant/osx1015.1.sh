#!/bin/bash

# disable screensaver
defaults -currentHost write com.apple.screensaver idleTime 0

# Turn Off System/Display/HDD Sleep
sudo systemsetup -setcomputersleep Never
sudo systemsetup -setdisplaysleep Never
sudo systemsetup -setharddisksleep Never

sudo sh -c "echo \"vagrant\\tUsers/vagrant/work\" >>/etc/synthetic.conf"
mkdir -p /Users/vagrant/work

sudo /usr/sbin/softwareupdate -l
sudo /usr/sbin/softwareupdate -ia
sudo /usr/sbin/softwareupdate -l

