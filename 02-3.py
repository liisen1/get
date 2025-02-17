import RPi.GPIO as GPIO
import time

leds = [2,3,4,17,27,22,10,9]
aux = [21,20,26,16,19,25,23,24]
GPIO.setmode(GPIO.BCM)

for i in leds:
    GPIO.setup(i, GPIO.OUT)
for i in aux:
    GPIO.setup(i, GPIO.IN)
    
while True:
    for i in range(len(aux)):
        if GPIO.input(aux[i]) == 1:
            GPIO.output(leds[i], 1)
        else:
            GPIO.output(leds[i], 0)