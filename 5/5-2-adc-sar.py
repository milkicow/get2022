import RPi.GPIO as malina
import time

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


t = 0.001
counter = 1

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    binary = [1, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, 8):

        binary[i] = 1
        malina.output(dac, binary)                
        time.sleep(t)
        comparatorValue = malina.input(comp)
        if comparatorValue == 0:
            binary[i] = 0
        else:
            binary[i] = 1
    
    return binary[0] * 2**7 + binary[1] * 2**6 + binary[2] * 2**5 + binary[3] * 2**4 + binary[4] * 2**3 + binary[5] * 2**2 + binary[6] * 2 + binary[7]


try:
    while True:
        voltage = adc() / levels * MaxVoltage
        print(voltage)

finally:
    malina.output(dac, 0)
    malina.output(troyka, 0)
    malina.cleanup()
     