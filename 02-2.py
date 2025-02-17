import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]
number = [0,1,0,0,1,1,1,0]
GPIO.setmode(GPIO.BCM)

for i in dac:
    GPIO.setup(i, GPIO.OUT)

for i in range(len(dac)):
    GPIO.output(dac[i], number[i])
time.sleep(15)

for i in dac:
    GPIO.output(i, 0)

GPIO.cleanup()