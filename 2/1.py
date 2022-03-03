import RPi.GPIO as malina
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

malina.setmode(malina.BCM)

malina.setup(leds, malina.OUT)

for i in range (3):
    for port in leds:
        malina.output(port, 1)
        time.sleep(0.2)
        malina.output(port, 0)

malina.output(leds, 0)

malina.cleanup()



