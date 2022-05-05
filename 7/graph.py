import numpy as np
import matplotlib.pyplot as plt
import textwrap as tw

v_max = 3.3

with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
dt = tmp[1]

data_array = np.loadtxt("data.txt", dtype=int)
data_array = v_max * data_array / 2**8
time = np.linspace(0, dt * (len(data_array) - 1), len(data_array))

fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.plot(time, data_array, label='V(t)', color='pink', linewidth=3) 
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, c")
wrap = tw.wrap("Процесс заряда и разряда конденсатора в RC-цепочке", width = 20)


ax.set_title("\n".join(wrap))
ax.legend(fontsize = 10,
          ncol = 1,   
          facecolor = 'oldlace',    
          edgecolor = 'r',    
          title = 'Данные',    
          title_fontsize = '10' 
         )
ax.grid(which='major',
        color = 'k')

ax.minorticks_on()

ax.grid(which='minor',
        color = 'royalblue',
        linestyle = ':')


yMax = np.max(data_array)
ax.set_xlim([0, dt * (len(data_array) - 1)])
ax.set_ylim([0, yMax + 0.5])

vMax = np.argmax(data_array)
t1 = time[vMax]
t2 = time[-1] - t1

x_text = t1 + (time[-1]-t1)/2

y_text = yMax / 2 


ax.text(x_text, y_text + 0.5, "Время зарядки " + str(round(t1, 3)))
ax.text(x_text, y_text, "Время разрядки " + str(round(t2, 3)))


fig.savefig("save.svg")
