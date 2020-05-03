#!/bin/sh

# config.vm.synced_folder ".", "/vagrant", type: "rsync",
#   rsync__exclude: [".git/",".tox/"],
#   owner: "vagrant",  group: "wheel"

#   $script = "
#   cd /vagrant/vagrant
#   sudo -u vagrant -H ./osx.sh
#   "

#autologin
brew tap xfreebird/utils
brew install kcpassword
enable_autologin "vagrant" "vagrant"

# disable screensaver
defaults -currentHost write com.apple.screensaver idleTime 0

# Turn Off System/Display/HDD Sleep
sudo systemsetup -setcomputersleep Never
sudo systemsetup -setdisplaysleep Never
sudo systemsetup -setharddisksleep Never


brew install python3 imagemagick wxmac pyqt pyside gdk-pixbuf gtk+3 mc pqiv pidof
brew cask install xquartz
python3 -m pip install --user pillow qtpy wxpython pyobjc-framework-Quartz pyobjc-framework-LaunchServices nose path.py tox

sudo chown -R vagrant /vagrant
sudo reboot