#!/bin/bash

DIR='/proc/asound/card0/pcm0p/sub0/status'
CMD='python /home/pi/furby/furby.py'

content=''
while true
do
	new_content=`cat $DIR`
	if [[ "$content" != "$new_content" ]]; then
		content=$new_content
		$CMD
	fi
	sleep 0.25
done
