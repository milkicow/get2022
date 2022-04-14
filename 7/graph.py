import matplotlib.pyplot as mat
import random

data = [random.randint(0, 50) for i in range(20)]
print(data)
mat.plot(data)
data_str = list(map(str, data))

with open('data.txt', 'w') as out:
    out.write('\n'.join(data_str))

mat.show()