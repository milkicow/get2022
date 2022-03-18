import RPi.GPIO as malina

dac = [26, 19, 13, 6, 5, 11, 9, 10]

malina.setmode(malina.BCM)

malina.setup(dac, malina.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while(1):
        num = input("enter int number in [0, 255]:")
        if num == 'q':
            break
        elif num.isdigit() is False:
            try:
                num = float(num)
                print("float number")
            except ValueError:
                print("string")    
        else:     
            try:
                num = int(num)
            except ValueError:
                print("not int num")
        
        
            if 0 <= num <= 255:
                print("voltage = ", num * 3.3/256)
                malina.output(dac, decimal2binary(num))
            else:
                print("input num not in range [0, 255]")
                if num < 0:
                    print("num < 0")
                if num > 255:
                    print("exceeds the capacity (num > 255)")
        


finally:
    malina.output(dac, 0)
    malina.cleanup()