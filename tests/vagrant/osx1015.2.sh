#!/bin/bash

export CI=1
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#autologin
brew tap xfreebird/utils
brew install kcpassword
enable_autologin "vagrant" "vagrant"


brew install wxwidgets 

brew install pidof 
brew install mc  htop
brew install imagemagick 
# brew install pyqt pyqt@5 
# brew install pyside  pyside@2
brew install gdk-pixbuf gtk+3 
# brew install python-tk
# brew install pqiv 

#brew cask install xquartz
python3 -m pip install --user pillow wxpython pyobjc-framework-Quartz pyobjc-framework-LaunchServices pytest tox

