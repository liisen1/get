import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
p = GPIO.PWM(20, 100)
p.start(0)

try:
    while True:
        dc = float(input())
        p.ChangeDutyCycle(dc)
        voltage = 3.3 * dc / 100
        print(voltage, 'V')

finally:
    p.stop()
    GPIO.cleanup()