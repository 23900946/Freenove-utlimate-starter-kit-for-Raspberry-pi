import os
import sys
import time
import RPi.GPIO as GPIO

Buzzer = 11
Button = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Button, GPIO.IN)
GPIO.setup(Buzzer, GPIO.OUT)

try:
    while True:
        if GPIO.input(Button) == GPIO.HIGH:
            GPIO.output(Buzzer, GPIO.HIGH)
            print("Doorbell ringing")
            time.sleep(1)
          
        
        else:
            GPIO.output(Buzzer, GPIO.LOW)
            
except KeyboardInterrupt:
    GPIO.cleanup()
        