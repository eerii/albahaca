import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_b as rl
import mpl_config as mpl

mpl.inicio(3, [3, 2.2])

#Datos
m1 = 0.20401
m2 = 0.23003
m3 = 0.33012
L = 0.1 #Diafragma
m = 0.02977

sm = 0.00001
st = 0.001
sl = 0.001

d = [pd.read_csv("LN_MRUA_M{}.csv".format(i), sep=';', decimal=',') for i in range(1,4)]
S = np.array([d[j]["S"] for j in range(0,3)])
T = np.array([d[j]["T"] for j in range(0,3)])
T2 = np.array([d[j]["T2"] for j in range(0,3)])

c = ["royalblue", "mediumseagreen", "tomato"]

#METODO 1
Ta = (1/2) * T**2

#Gráficas
for i in range(3):
    plt.clf()

    #Gráficas
    plt.scatter(Ta[i], S[i], color=c[i], edgecolors="black", linewidth=0.5)

    #Ajuste
    b = rl(Ta[i], S[i])[0]
    xr = np.linspace(min(Ta[i]), max(Ta[i]), 10)
    yr = b*xr
    plt.plot(xr, yr, color=c[i])

    #mpl.guardar("LN_MRUA_L{}".format(i+1), "$T^2/2(s)$", "S(m)", False)

#METODO 2
V2 = L / T2
sV2 = ((sl**2 / T2**2) + ((L**2 * st**2) / T2**4))**0.5

Lu = unc.ufloat(L, sl)
T2u = unp.uarray(T2, st)
V2u = Lu / T2u

for i in range(len(V2u)):
    for j in range(len(V2u[i])):
        print("V-{}-{} = {:.2u}".format(i, j, V2u[i,j]))

for i in range(3):
    plt.clf()

    #Gráficas
    plt.scatter(T[i], V2[i], color=c[i], edgecolors="black", linewidth=0.5)

    #Ajuste
    b = rl(T[i], V2[i])[0]
    xr = np.linspace(min(T[i]), max(T[i]), 10)
    yr = b*xr
    plt.plot(xr, yr, color=c[i])

    mpl.guardar("LN_MRUA_A{}".format(i+1), "$T(s)$", "V(m/s)", False)

#TEORICO
g = unc.ufloat(9.8, 0.1)
a1 = g * (m/m1); a2 = g * (m/m2); a3 = g * (m/m3)
sa = lambda M: sm * ((g/M)**2 + ((g*m) / M**2)**2)**0.5
sa1 = sa(m1); sa2 = sa(m2); sa3 = sa(m3)

Mu = unp.uarray([m1, m2, m3], sm); mu = unc.ufloat(m, sm)
au = g*(mu / Mu)

for i in range(3):
    print("A = {:.2u}".format(au[i]))
np.savetxt("LN_MRUA_VA.csv", au, "%r", delimiter=";")
