#!/usr/bin/env python

import os
import discord
import subprocess
from dotenv import load_dotenv
import time
import RPi.GPIO as GPIO
import time
import os
from datetime import datetime
from ruuvitag_sensor.ruuvitag import RuuviTag

load_dotenv()
mac = os.getenv('RUUVI_MAC')
sensor = RuuviTag(mac)

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


def move():
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

def gettemp():
	data = sensor.update()
	temp = data['temperature']
	os.system('espeak "The temperature here is '+str(temp)+' degrees celsius."')
	return temp

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	os.system('espeak "Connected to discord."')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.channel.id == 731885964745769021:
		if not message.content.startswith('!'):
			move()
			os.system('espeak "'+ message.content +'"')
			move()
		else:
			if 'temp' in message.content:
				move()
				await message.channel.send(str(gettemp()).split('.')[0] + '\u00b0C')
				move()
client.run(TOKEN)
