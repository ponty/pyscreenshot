#!/bin/sh

# autologin
echo '
[SeatDefaults]
autologin-user=vagrant
' >> /etc/lightdm/lightdm.conf.d/12-autologin.conf

sudo systemctl start lightdm

