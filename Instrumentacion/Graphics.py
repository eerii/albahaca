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

name = "CC6"

#Read from CSV to pandas dataframe
d = pd.read_csv(name + ".csv", sep=';', decimal=',')
#print(d)
x = d["i"]
y = d["v"]
n = d.shape[0]
a, b = 0, 0

y1 = d["v1"]
y2 = d["v2"]
y3 = d["v3"]

regresionLineal = True;

#Linear regression
def reg_lin(x, y, n):
    sx = x.sum()
    sy = y.sum()
    sxy = (x*y).sum()
    sx2 = (x**2).sum()

    print("sx=",sx,"sy=", sy)
    print("sxy=", sxy, "sx2=", sx2)

    a = (sy*sx2 - sx*sxy) / (n*sx2 - sx**2)
    b = (n*sxy - sx*sy) / (n*sx2 - sx**2)

    sdesv = ((y - a - b*x)**2).sum()
    s = (sdesv/float(n-2))*0.5
    sa = s*(sx2 / (n*sx2 - sx**2))**0.5
    sb = s*(n / (n*sx2 - sx**2))**0.5

    sy2 = (y**2).sum()
    r = (n*sxy - sx*sy)/(((n*sx2 - sx**2)*(n*sy2 - sy**2))**0.5)

    return a, b, s, sa, sb, r

#Scatter Plot
fig = plt.figure()
fig.set_size_inches(w=5, h=3.5)

def plot(x, y, n, cc="#1f77b4", cr="skyblue"):
    a, b, s, sa, sb, r = reg_lin(x, y, n)

    print("a=", a,"b=", b)
    print("s=", s,"sa=", sa, "sb=", sb)
    print("r=", r)

    xr = np.linspace(1, 13, 10)
    yr = (a + b*xr) / (10**6)

    plt.plot(xr, yr, color=cr, zorder=1)
    plt.scatter(x * (10**6), y, color=cc, zorder=2)

plot(x, y, n)
plot(x, y1, n, "tomato", "lightsalmon")
plot(x, y2, n, "gold", "moccasin")
plot(x, y3, n, "limegreen", "lightgreen")

plt.ylabel('V(V)', rotation=0, labelpad=20)
plt.xlabel('I($\mu$A)')
#plt.title('Voltaje (V) frente a intensidad (I)')
plt.savefig(name + ".pgf", bbox_inches = "tight")
