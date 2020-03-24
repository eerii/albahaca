import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Configure matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

name = "CA4"

#Read from CSV to pandas dataframe
d = pd.read_csv(name + ".csv", sep=';', decimal=',')

x = d["f"]
vmr = d["VmR"]
vmc = d["VmC"]
y = vmr / vmc

#Scatter Plot
fig = plt.figure()
fig.set_size_inches(w=5, h=3.5)

plt.scatter(x,y, zorder=2)

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, zorder=1, color="skyblue")
x2 = (1 - b)/m
plt.scatter(x2, 1, zorder=3, color="tomato")
print("Frecuencia corte:", x2)

plt.ylabel('VmR/VmC', rotation=0, labelpad=25)
plt.xlabel('f (Hz)')
#plt.title('Voltaje (V) frente a intensidad (I)')
plt.savefig(name + "V.pgf", bbox_inches = "tight")
