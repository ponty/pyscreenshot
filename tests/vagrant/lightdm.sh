#!/bin/sh

# autologin
echo '
[SeatDefaults]
autologin-user=vagrant
' >> /etc/lightdm/lightdm.conf.d/12-autologin.conf

sudo systemctl enable lightdm
sudo systemctl start lightdm

