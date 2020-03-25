import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

#Configure matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

name = "CA4Alt"

#Read from CSV to pandas dataframe
d = pd.read_csv(name + "All.csv", sep=';', decimal=',')

x = d["logf"]
vm = d["VmRVmC"]
y = np.rad2deg(np.arctan(-(1/vm)))

#Scatter Plot
fig = plt.figure()
fig.set_size_inches(w=5, h=3.5)

plt.scatter(x,y, zorder=2)

#Ajuste a arctan
def farctan(x, a, b, c):
    xrad = np.deg2rad(x)
    return a * np.rad2deg(np.arctan(b * xrad)) + c

y2 = (y + 45)
x2 = x - 3.1226

popt, pcov = curve_fit(farctan, x2, y2)

xs = np.arange(-1.5, +1., 0.001)
ys = (farctan(xs, *popt)) - 45
xs += 3.1226
plt.plot(xs, ys, color="gold")

for i in range(len(ys)):
    if ys[i] < -44.95 and ys[i] > -45.05:
        plt.scatter(xs[i], ys[i], color="tomato", zorder=4)
        print("Frecuencia de corte:", xs[i], 10**xs[i])


#print("Frecuencia corte:", x3, 10**x3)

plt.ylabel('$\\phi$ \\textit{(º)}', rotation=0, labelpad=25)
plt.xlabel('log f')
#plt.title('Voltaje (V) frente a intensidad (I)')
plt.savefig(name + "Arctan.pgf", bbox_inches = "tight")
