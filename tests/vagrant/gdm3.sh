#!/bin/sh

sudo apt-get install -y gdm3

# autologin
echo '
[daemon]
AutomaticLoginEnable = true
AutomaticLogin = vagrant
' > /etc/gdm3/custom.conf

sudo systemctl start gdm3


