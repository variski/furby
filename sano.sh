#!/bin/sh

sudo python /home/pi/furby/onemove.py
for ARG in "$@"; do
	espeak -vfi+f1 "$ARG" 2>/dev/null
done
sudo python /home/pi/furby/onemove.py
