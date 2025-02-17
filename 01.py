import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

f = GPIO.input(26)
if f == 1:
    GPIO.output(20, 1)
else:
    GPIO.output(20, 0)
