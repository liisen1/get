import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def adc():
    for val in range(256):
        bin_val = dec2bin(val)
        GPIO.output(dac, bin_val)
        time.sleep(0.007)
        if GPIO.input(comp) == 1:
            return val
    return 255

dac = [8,11,7,1,0,5,12,6]
leds = [2,3,4,17,27,22,10,9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        adc_val = adc()
        voltage = adc_val * 3.3 / 256
        num_leds = min(int((adc_val / 255) * 8), 8)
        state = [0] * 8
        for i in range(num_leds):
            state[7 - i] = 1
        GPIO.output(leds, state)
        print(voltage, 'V')
        time.sleep(0.1)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()