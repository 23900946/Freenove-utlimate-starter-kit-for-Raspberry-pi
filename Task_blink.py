import os
import sys
import time
import RPi.GPIO as GPIO

LEDRed = 11


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDRed, GPIO.LOW)

def blink():
    while True:
        GPIO.output(LEDRed, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LEDRed, GPIO.LOW)
        time.sleep(1)
        

blink()