import os
import sys
import time
import RPi.GPIO as GPIO


LEDpins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LEDpins, GPIO.OUT)

while True:
    for pins in LEDpins: # Makes each LED blink once
        GPIO.output(pins, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pins, GPIO.HIGH)
        
    for pins in LEDpins[::-1]: # Makes each LED blink once but in reverse order
        GPIO.output(pins, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pins, GPIO.HIGH)
