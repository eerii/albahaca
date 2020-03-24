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

name = "CA4Alt"

#Read from CSV to pandas dataframe
d = pd.read_csv(name + ".csv", sep=';', decimal=',')
dextra = pd.read_csv(name + "All.csv", sep=';', decimal=',')
#print(d)
logfcsv = d["logf"]
logzcsv = d["20logZ"]

r = 10**4
f = d["f"]
vm = d["Vm"]
vmr = d["VmR"]
fe = dextra["f"]
vme = dextra["Vm"]
vmre = dextra["VmR"]

logf = np.log10(f)
logfe = np.log10(fe)
logzfunc = lambda v1, v2: 20 * np.log10(r * (v1 / v2))
logz = logzfunc(vm, vmr)
logze = logzfunc(vme, vmre)

#Scatter Plot
fig = plt.figure()
fig.set_size_inches(w=5, h=3.5)

def plot(x, y, z=0, cc="#1f77b4"):
    plt.scatter(x, y, color=cc, zorder=z)

def asintotas(f, v1, v2):
    x = np.log10(f)
    #Curva R
    yr = np.ones(v1.shape[0])
    yr *= 20 * np.log10 (r)
    plt.plot(x, yr, color="tomato", zorder=0)
    #Curva C
    c = 1.2 * 10**-8
    z = 1 / (2 * np.pi * f * c)
    yc = 20 * np.log10(z)
    plt.plot(x, yc, color="gold", zorder=0)
    #Intersección
    m1, b1 = 0, yr[0]
    m2, b2 = np.polyfit(x, yc, 1)
    xint = (b2 - b1) / (m1 - m2)
    yint = m1 * xint + b1
    print("m1: {}, b1:{}, m2:{}, b2:{}".format(m1, b1, m2, b2))
    print("Intersección: x", xint, "y", yint)
    plt.scatter(xint, yint, color="dodgerblue", zorder=3)


plot(logf, logz, 2)
#plot(logfe, logze, 1, "skyblue")
asintotas(f, vm, vmr)
#asintotas(fe, vme, vmre)

plt.ylabel('20log Z', rotation=0, labelpad=20)
plt.xlabel('log f')
#plt.title('Voltaje (V) frente a intensidad (I)')
plt.savefig(name + "R.pgf", bbox_inches = "tight")
