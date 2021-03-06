#!/usr/bin/env python

# Import required modules
import time
import os
import subprocess
import RPi.GPIO as GPIO
from dotenv import load_dotenv

load_dotenv()

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(15, GPIO.OUT) # Connected to AIN2
GPIO.setup(16, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY

# Drive the motor clockwise
GPIO.output(16, GPIO.HIGH) # Set AIN1
GPIO.output(15, GPIO.LOW) # Set AIN2
GPIO.output(13, GPIO.HIGH) # Set STBY

# Wait and stop
time.sleep(0.5)
GPIO.output(13, GPIO.LOW)
time.sleep(1)

# speak & wait
subprocess.call(['aplay', os.getenv('SOUND_HI')], shell=False)
time.sleep(1)

# Drive the motor counterclockwise
GPIO.output(16, GPIO.LOW) # Set AIN1
GPIO.output(15, GPIO.HIGH) # Set AIN2
GPIO.output(13, GPIO.HIGH) # Set STBY

# Wait & speak
time.sleep(1)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(16, GPIO.LOW) # Set AIN1
GPIO.output(15, GPIO.LOW) # Set AIN2
GPIO.output(13, GPIO.LOW) # Set STBY

subprocess.call(['aplay', os.getenv('SOUND_ACTIVATED')], shell=False)
