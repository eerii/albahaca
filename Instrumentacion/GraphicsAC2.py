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

name = "CA5"

#Read from CSV to pandas dataframe
d = pd.read_csv(name + ".csv", sep=';', decimal=',')
d2 = pd.read_csv(name + "All.csv", sep=';', decimal=',')

x = d["logf"]
y = d["phideg"]
x2 = d2["logf"]
y2 = d2["phideg"]
#vmr = d["VmR"]
#vmc = d["VmC"]
#y = vmr / vmc

#Scatter Plot
fig = plt.figure()
fig.set_size_inches(w=5, h=3.5)

plt.scatter(x,y, zorder=2)
plt.scatter(x2,y2, zorder=1, color="dodgerblue")

#Ajuste a recta
#m, b = np.polyfit(x2, y2, 1)
#plt.plot(x, m*x + b, zorder=1, color="skyblue")
#x3 = (-45 - b)/m
#plt.scatter(x3, -45, zorder=3, color="tomato")


#Ajuste a polinomio
#p2 = np.polynomial.Polynomial.fit(x2, y2, 2)
#p3 = np.polynomial.Polynomial.fit(x2, y2, 3)
#p4 = np.polynomial.Polynomial.fit(x2, y2, 4)
#p5 = np.polynomial.Polynomial.fit(x2, y2, 5)
#plt.plot(*p2.linspace(), color="tomato")
#plt.plot(*p3.linspace(), color="gold")
#plt.plot(*p4.linspace(), color="limegreen")
#plt.plot(*p5.linspace(), color="skyblue")

#Ajuste a sigmoide
def fsigmoid(x, a, b):
    return 1.0 / (1.0 + np.exp(-a*(x-b)))

y3 = (y2 + 100) * 0.01
x3 = x2 - 3.1226

popt, pcov = curve_fit(fsigmoid, x3, y3, method='dogbox')

xs = np.arange(-3., +3., 0.01)
ys = (fsigmoid(xs, *popt) * 100) - 100
xs += 3.1226
#plt.plot(xs, ys, color="gold")


#Ajuste a arctan
def farctan(x, a, b, c):
    xrad = np.deg2rad(x)
    return a * np.rad2deg(np.arctan(b * xrad)) + c

y3 = (y2 + 45)
x3 = x2 - 3.1226

popt, pcov = curve_fit(farctan, x3, y3)

xs = np.arange(-2.5, +2., 0.01)
ys = (farctan(xs, *popt)) - 45
xs += 3.1226
plt.plot(xs, ys, color="gold")

for i in range(len(ys)):
    if ys[i] < -44.5 and ys[i] > -45.5:
        plt.scatter(xs[i], ys[i], color="tomato", zorder=4)
        print("Frecuencia de corte:", xs[i], 10**xs[i])


#print("Frecuencia corte:", x3, 10**x3)

plt.ylabel('$\\phi$ \\textit{(º)}', rotation=0, labelpad=25)
plt.xlabel('log f')
#plt.title('Voltaje (V) frente a intensidad (I)')
plt.savefig(name + "Arctan.pgf", bbox_inches = "tight")
