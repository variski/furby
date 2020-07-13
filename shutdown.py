#!/usr/bin/env python3

from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO
import subprocess

load_dotenv()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(4, GPIO.FALLING)
	subprocess.call(['aplay', os.getenv('SOUND_SHUTDOWN')], shell=False)
	subprocess.call(['shutdown', '-h', 'now'], shell=False)
except:
	pass
