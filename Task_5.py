import os
import sys
import time
import random
import RPi.GPIO as GPIO

LED = [11, 12, 13]

global pwmRed, pwmGreen, pwnBlue

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.HIGH)
pwmRed = GPIO.PWM(LED[0], 2000)      
pwmGreen = GPIO.PWM(LED[1], 2000)  
pwmBlue = GPIO.PWM(LED[2], 2000)    
pwmRed.start(0)      
pwmGreen.start(0)
pwmBlue.start(0)

def colour(red, green, blue):
    pwmRed.ChangeDutyCycle(red)     
    pwmGreen.ChangeDutyCycle(green)   
    pwmBlue.ChangeDutyCycle(blue)
    
def loop():
    while True:
        r=random.randint(0,100)  
        g=random.randint(0,100)
        b=random.randint(0,100)
        colour(r,g,b)          
        time.sleep(1)
        
loop()