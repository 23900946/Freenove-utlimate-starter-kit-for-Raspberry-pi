import time
from ADCDevice import *

adc = ADCDevice()

def config():
    global adc
    
    if(adc.detectI2c(0x48)):
        adc = PCF8951()
    
    elif(adc.detectI2c(0x4b)):
        adc = ADS7830()
        
    else:
        print("No/Incorrect address found")
        exit(-1)
        
def cycle():
    while True:
        value = adc.analogRead(0) 
        voltage = value / 255.0 * 3.3 
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.1)
         
def end():
    adc.close()
         

try:
    config()
    cycle()
 
except KeyboardInterrupt: 
    destroy()