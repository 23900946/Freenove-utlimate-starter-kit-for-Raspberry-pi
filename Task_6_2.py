import os
import sys
import time
import RPi.GPIO as GPIO
import math

Buzzer = 11
Button = 12

global p
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Buzzer, GPIO.OUT)
p = GPIO.PWM(Buzzer, 1) 
p.start(0)

def alarm():
    p.start(50)
    for x in range(0, 361):
        sinVal = math.sin(x * (math.pi / 180.0))
        toneVal = 2000 + sinVal * 500
        p.ChangeFrequency(toneVal)
        time.sleep(0.001)

def stopAlarm():
    p.stop()

try:
    while True:
        if GPIO.input(Button) == GPIO.LOW:
            alarm()
            print("Alarm going off")
            time.sleep(1)
          
        
        else:
            stopAlarm()
            
except KeyboardInterrupt:
    GPIO.cleanup()