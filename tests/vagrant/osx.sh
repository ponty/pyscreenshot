#!/bin/bash
set -e

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

# Warning: A newer Command Line Tools release is available.
# Update them from Software Update in System Preferences or run:
# softwareupdate --all --install --force

# Error: 
#  homebrew-core is a shallow clone.
# To `brew update`, first run:
git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow

brew install openssl@1.1
brew install python3 
brew install wxwidgets 

brew install pidof 
# brew install mc  htop
brew install imagemagick 
# brew install pyqt pyqt@5 
# brew install pyside  pyside@2
brew install gdk-pixbuf gtk+3 
# brew install python-tk
# brew install pqiv 

#brew cask install xquartz
python3 -m pip install --user pillow wxpython pyobjc-framework-Quartz pyobjc-framework-LaunchServices pytest tox

sudo chown -R vagrant /vagrant
