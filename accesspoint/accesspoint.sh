#!/bin/bash

# install access point stuff, adapted from https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md
apt install -y hostapd dnsmasq
systemctl unmask hostapd
systemctl enable hostapd
DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent

echo "interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant" >> /etc/dhcpcd.conf
    
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
echo "interface=wlan0 # Listening interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
                # Pool of IP addresses served via DHCP
domain=wlan     # Local wireless DNS domain
address=/gw.wlan/192.168.4.1
                # Alias for this router" >> /etc/dnsmasq.conf
                
rfkill unblock wlan
echo "country_code=US
interface=wlan0
ssid=Furby
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=gofurbygo
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP" >> /etc/hostapd/hostapd.conf

systemctl reboot
