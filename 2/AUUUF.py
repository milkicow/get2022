import RPi.GPIO as malina
#import time
#import random

leds = [21, 20, 16, 12, 7, 8, 25, 24]

auf = [22, 23, 27, 18, 15, 14, 3, 2]

malina.setmode(malina.BCM)

malina.setup(leds, malina.OUT)

malina.setup(auf, malina.IN)




try:
    while (1):
        for i in range (8):
            malina.output(leds[i], malina.input(auf[i]))
    

finally:

    malina.output(leds, 0)

    malina.cleanup()