import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy

#Leer datos
d1 = pd.read_csv("BH-4.csv", sep=';', decimal=',')
I1 = d1["I"]
Be1 = d1["Bexp"]
d2 = pd.read_csv("BH-5.csv", sep=';', decimal=',')
I2 = d2["I"]
Be2 = d2["Bexp"]
d3 = pd.read_csv("BH-6.csv", sep=';', decimal=',')
I3 = d3["I"]
Be3 = d3["Bexp"]

#Regresión lineal sin término independiente
def reg_lin(x, y):
    n = len(x)

    sxy = (x*y).sum()
    sx2 = (x**2).sum()

    b = sxy / sx2

    sybx = ((y - b*x)**2).sum()
    s = (sybx / (n-1))**0.5
    sb = s / (sx2)**0.5

    sy2 = (y**2).sum()
    r = sxy / (sx2 * sy2)**0.5

    print("b=", b)
    print("s=", s, "sb=", sb)
    print("r=", r)

    return b

b1 = reg_lin(I1, Be1)
xr1 = np.linspace(min(I1), max(I1), 10)
yr1 = b1 * xr1
b2 = reg_lin(I2, Be2)
xr2 = np.linspace(min(I2), max(I2), 10)
yr2 = b2 * xr2
b3 = reg_lin(I3, Be3)
xr3 = np.linspace(min(I3), max(I3), 10)
yr3 = b3 * xr3

#Gráficas
plt.plot(xr1, yr1)
plt.plot(xr2, yr2)
plt.plot(xr3, yr3)

R = 0.2
N = 154
a, r, n, m = sy.symbols("a r n m")
frac = 2 / (1 + ((a**2) / (4 * r**2)))**(3/2)
mu = ((2 * m * r) / n) * (1 / frac)
fmu = sy.lambdify([a, r, n, m], mu, "numpy")

mu1 = fmu(R, R, N, b1)
mu2 = fmu(R/2, R, N, b2)
mu3 = fmu(2*R, R, N, b3)

print("Permeabilidad orginal: {}, P1: {}, P2: {} P3:{}".format(4 * np.pi * 10**(-7), mu1, mu2, mu3))
