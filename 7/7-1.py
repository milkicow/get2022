import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def get_bin(value):

    return (1 << round(value/32)) - 1

def adc():
    Guess = [1, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(8):

        Guess[i] = 1
        GPIO.output(dac, Guess)
        time.sleep(0.01)
        compdata = GPIO.input(comp)
        if compdata == 0:
            Guess[i] = 0
        else:
            Guess[i] = 1
    value = Guess[0]*128 + Guess[1]*64 + Guess[2]*32 + Guess[3]*16 + Guess[4]*8 + Guess[5]*4 + Guess[6]*2 + Guess[7]

    GPIO.output(leds, decimal2binary(get_bin(value)))
    return value



GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
data = []
comp = 4
troyka = 17




GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
try:
    GPIO.output(troyka, 1)
    start = time.time()
    voltage = adc()
    while(voltage < 0.97*256):
        print("input voltage = {:.1f}".format(voltage))
        data.append(voltage)
        voltage = adc()
        
    GPIO.output(troyka, 0)

    while(voltage > 0.03 * 256):
        print("input voltage = {:.1f}".format(voltage))
        data.append(voltage)
        voltage = adc()
    finish = time.time()

    with open("settings.txt", "w") as stn:
        stn.write("{:.2f}\n".format(len(data)/(finish - start)))
        stn.write("{:.2f}".format(1))

    print("Время измерения = {:.2f}".format(finish - start))
    print("Частота дескретизации = {:.2f}".format(len(data)/(finish - start)))
    print("Период = {:.2f}".format((finish - start)/len(data)))
    print("Шаг квантования = {:.2f}".format(3.3/256))

    print(" = {:.2f}".format(finish - start))  

    plt.plot(data)
    plt.show()
    data_str = [str(item) for item in data]
    

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(data_str))

except ArithmeticError:
    print ("Arithmetic")

except KeyboardInterrupt:
    print ("KeyboardInterrupt")
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()  
