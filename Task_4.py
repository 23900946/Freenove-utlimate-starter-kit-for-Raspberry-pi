import os
import sys
import time
import RPi.GPIO as GPIO

LEDred = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LEDred, GPIO.OUT)
GPIO.output(LEDred, GPIO.LOW)

p = GPIO.PWM(LEDred, 500)     
p.start(0)     

while True:
    for dc in range(0, 101, 1):   #Makes the led brighter
            p.ChangeDutyCycle(dc)     
            time.sleep(0.01)
    time.sleep(1)
    for dc in range(100, -1, -1): #Makes the led darker
        p.ChangeDutyCycle(dc)     
        time.sleep(0.01)
    time.sleep(1)
        

    