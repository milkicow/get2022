import RPi.GPIO as malina

malina.setmode(malina.BCM)

malina.setup(2, malina.OUT)

malina.setup(3, malina.IN)

malina.output(2, malina.input(3))