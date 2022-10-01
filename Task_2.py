import os
import sys
import time
import RPi.GPIO as GPIO

LEDRed = 11
Button = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(Button, GPIO.IN)

while True: 
    if GPIO.input(Button) == False: # LED will switch on when button is pressed
        print("Button pressed")
        GPIO.output(LEDRed, GPIO.HIGH)
        
    else:
        GPIO.output(LEDRed, GPIO.LOW) # LED will be in a off state until button is pressed
        os.system('clear')
        print("Waitng for button press")
        
    time.sleep(2)

