#!/bin/sh
# disables access point and enables wifi

systemctl stop hostap
sed -i '62,64 s/^/#/' /etc/dhcpcd.conf
reboot
