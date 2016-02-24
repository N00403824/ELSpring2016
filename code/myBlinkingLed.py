#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def Blink(blinks):
    for i in range(0,blinks):
	GPIO.output(17,True)
    	time.sleep(0.25)
    	GPIO.output(17,False)
	time.sleep(0.25)
try:
    while True:
   	for blink in range(3,5):	
	    Blink(blink)
            time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
