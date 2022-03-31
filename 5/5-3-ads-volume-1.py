import RPi.GPIO as malina
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
MaxVoltage = 3.3
bits = 8
levels = 2**bits


malina.setmode(malina.BCM)
malina.setup(dac, malina.OUT)
malina.setup(troyka, malina.OUT, initial = 1)
malina.setup(comp, malina.IN)
malina.setup(leds, malina.OUT)


t = 0.001

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range (levels):

        malina.output(dac, decimal2binary(i))                
        time.sleep(t)
        comparatorValue = malina.input(comp)
        if comparatorValue == 0:
            print(i)
            return i

try:
    while True:
        kek = round(adc() / 256 * 8)

        malina.output(leds, decimal2binary(2**kek - 1))
        voltage = adc() / levels * MaxVoltage
        # print("voltage = {:.2f}".format(voltage))
        print(voltage)

finally:
    malina.output(dac, 0)
    malina.output(troyka, 0)
    malina.cleanup()
     