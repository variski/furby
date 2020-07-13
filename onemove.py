#!/usr/bin/env python

# Import required modules
import time
import os
import subprocess
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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

# Reset all the GPIO pins by setting them to LOW
GPIO.output(16, GPIO.LOW) # Set AIN1
GPIO.output(15, GPIO.LOW) # Set AIN2
GPIO.output(13, GPIO.LOW) # Set STBY
