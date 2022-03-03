import RPi.GPIO as malina
import time
import random

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 1, 0, 1]

malina.setmode(malina.BCM)

malina.setup(dac, malina.OUT)

#for i in range (8):
#    number.append(random.randint(0, 1))

malina.output(dac, number)

time.sleep(10)

malina.output(dac, 0)

malina.cleanup()