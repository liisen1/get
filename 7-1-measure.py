import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

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
    measures = []
    start_time = time.time()
    GPIO.output(troyka, GPIO.HIGH)

    voltage = 0

    while voltage < 175:
        voltage = adc()
        measures.append(voltage)
        GPIO.output(leds, dec2bin(voltage))

    GPIO.output(troyka, GPIO.LOW)

    while voltage > 120:
        voltage = adc()
        measures.append(voltage)
        GPIO.output(leds, dec2bin(voltage))
    
    final_time = time.time()
    duration = final_time - start_time
    sampling_rate = len(measures) / duration
    quantization_step = 3.3 / 256

    print(f"Общая продолжительность:{duration}")
    print(f"Период измерения:{duration / len(measures)}")
    print(f"Средняя частота дискретизации:{sampling_rate}")
    print(f"Шаг квантования:{quantization_step}")

finally:
    for i in measures:
        i = i*3.3/256

    str_measures = [str(i) for i in measures]

    with open('data.txt', 'w') as f:
        f.write("\n".join(str_measures))

    with open('settings.txt', 'w') as file:
        file.write(f"Средняя частота дискретизации:{sampling_rate}\n")
        file.write(f"Шаг квантования:{quantization_step}\n")

    plt.plot(measures)
    plt.show()

    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()