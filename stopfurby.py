import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# Turn off GPIO warnings caused by us declaring our pins outside of the start_furby and stop_furby functions
GPIO.setwarnings(False)

# Set up GPIO pins
GPIO.setup(15, GPIO.OUT) # Connected to AIN2
GPIO.setup(16, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY

# Reset all the GPIO pins by setting them to LOW
GPIO.output(16, GPIO.LOW) # Set AIN1
GPIO.output(15, GPIO.LOW) # Set AIN2
GPIO.output(13, GPIO.LOW) # Set STBY
