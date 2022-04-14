import RPi.GPIO as malina
import time
import matplotlib.pyplot as plt

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
        #malina.output(leds, binary)
        if comparatorValue == 0:
            binary[i] = 0
        else:
            binary[i] = 1
    
    return  (binary[0] * 2**7 + binary[1] * 2**6 + binary[2] * 2**5 + binary[3] * 2**4 + binary[4] * 2**3 + binary[5] * 2**2 + binary[6] * 2 + binary[7])

data =[]


try:
    malina.output(troyka, 1)
    voltage = 3.3*adc()/256
    start = time.time()
    while(voltage < 0.8 * 3.3):
        print("in vol = {:.2f}".format(voltage))
        data.append(voltage)
        voltage = 3.3*adc()/256

        binary = decimal2binary(adc())
        malina.output(leds, binary)
    
    malina.output(troyka, 0)

    while(voltage > 0.2 * 3.3):
        print("in vol = {:.2f}".format(voltage))
        data.append(voltage)

        voltage = 3.3*adc()/256
    
    finish = time.time()
    print("time = {:.2f}".format(finish - start))
    #print("шаг дескретизации = {:.2f}".format((finish - start)/(len(data)))

    plt.plot(data)
    plt.show()

    data_str = [str(item) for item in data]

    with open("data.txt", "w") as out:
        out.write("\n".join(data_str))






finally:
    malina.output(dac, 0)
    malina.output(troyka, 0)
    malina.cleanup()
     