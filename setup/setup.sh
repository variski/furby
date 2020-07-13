#!/bin/bash

curl -sS https://get.pimoroni.com/speakerphat | bash

apt-get install espeak

apt-get install pulseaudio pulseaudio-module-bluetooth
usermod -a -G bluetooth pi

# https://www.raspberrypi.org/forums/viewtopic.php?t=235519

# bluetooth stuff
