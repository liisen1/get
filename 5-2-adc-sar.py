import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def adc():
    val = 0
    for bit in range(7, -1, -1):
        step = 2 ** bit
        val += step
        bin_val = dec2bin(val)
        GPIO.output(dac, bin_val)
        time.sleep(0.007)
        if GPIO.input(comp) == 1:
            val -= step
    return val

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        adc_val = adc()
        voltage = adc_val * 3.3 / 256
        print(voltage, 'V')
        time.sleep(0.1)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()