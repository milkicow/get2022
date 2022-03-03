import RPi.GPIO as malina
import time

malina.setmode(malina.BCM)

malina.setup(2, malina.OUT)

malina.output(2, 1)

time.sleep(1)

malina.output(2, 0)

time.sleep(1)

malina.output(2, 1)

time.sleep(1)

malina.output(2, 0)

time.sleep(1)

malina.output(2, 1)

time.sleep(1)

malina.output(2, 0)

time.sleep(1)

malina.output(2, 1)

time.sleep(1)

malina.output(2, 0)

time.sleep(1)

malina.output(2, 1)

time.sleep(1)

malina.output(2, 0)

time.sleep(1)

malina.output(2, 1)

time.sleep(1)

malina.output(2, 0)

