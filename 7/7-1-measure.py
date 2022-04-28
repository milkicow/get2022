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

#функция перевода в двоичное число
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

#функция выдающее значение с ацп
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
adc1 = []


try:
    malina.output(troyka, 1)
    voltage = 3.3*adc()/256
    start = time.time() #сохраняет время начала эксперимента

    #зарядка конденсатора
    while(voltage < 0.8 * 3.3):
        print("voltage = {:.2f}".format(voltage))
        data.append(voltage)
        adc1.append(adc())
        voltage = 3.3*adc()/256

        binary = decimal2binary(adc())
        malina.output(leds, binary)
    
    malina.output(troyka, 0)

    #разрядка
    while(voltage > 0.1 * 3.3):
        print("voltage = {:.2f}".format(voltage))
        data.append(voltage)
        adc1.append(adc())

        voltage = 3.3*adc()/256
    
    finish = time.time() #сохраняет время конца эксперимента

    #Печать в файл часты дискретизации и шага квантования

    with open("out.txt", "w") as out:
        out.write("{:.2f}\n".format(len(data)/(finish - start)))
        out.write("{:.2f}".format(1*3.3/256))


    #Печать в терминал параметры проведенных измерений
    print("Время измерения = {:.2f}".format(finish - start))
    print("Частота дескретизации = {:.2f}".format(len(data)/(finish - start)))
    print("Период = {:.2f}".format((finish - start)/len(data)))
    print("Шаг квантования = {:.2f}".format(3.3/256))

    #рисует график
    plt.plot(data)
    plt.show()
    

    #заполняет файл измерениями ацп
    adc1_str = [str(item) for item in adc1]
    

    with open("adc.txt", "w") as outfile:
       outfile.write("\n".join(adc1_str))

except KeyboardInterrupt:
    print("KeyboardInterrupt")


finally:
    malina.output(dac, 0)
    malina.output(troyka, 0)
    malina.cleanup()
     