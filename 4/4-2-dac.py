import RPi.GPIO as malina
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

malina.setmode(malina.BCM)

malina.setup(dac, malina.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while 1:

        t = float(input("enter period: "))

        t = t/256
        if t == 'q':
            break
        else:
            
            while 1:
                for i in range (0, 255):

                    malina.output(dac, decimal2binary(i))                
                    time.sleep(t)

                for i in range (255, 0, -1):

                    malina.output(dac, decimal2binary(i))                       
                    time.sleep(t)



except ValueError():
    print("error input")

finally:
    malina.output(dac, 0)
    malina.cleanup()