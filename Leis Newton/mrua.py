import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_b as rl
import mpl_config as mpl

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

#METODO 1
Ta = (1/2) * T**2

#Gráficas
#plt.scatter(Ta[0], S[0])

#Ajuste
b = rl(Ta[0], S[0])[0]
xr = np.linspace(min(Ta[0]), max(Ta[0]), 10)
yr = b*xr
#plt.plot(xr, yr)

#METODO 2
V2 = L / T2
sV2 = ((sl**2 / T2**2) + ((L**2 * st**2) / T2**4))**0.5

Lu = unc.ufloat(L, sl)
T2u = unp.uarray(T2, st)
V2u = Lu / T2u

print("---\nPropEr V2 = {} +/- {}".format(V2[0,2], sV2[0,2]))
print("Uncert V2 = {:.2u}".format(V2u[0,2]))

#Gráficas
plt.scatter(T[0], V2[0])

#Ajuste
b = rl(T[0], V2[0])[0]
xr = np.linspace(min(T[0]), max(T[0]), 10)
yr = b*xr
plt.plot(xr, yr)

#TEORICO
g = 9.8
a1 = g * (m/m1); a2 = g * (m/m2); a3 = g * (m/m3)
sa = lambda M: sm * ((g/M)**2 + ((g*m) / M**2)**2)**0.5
sa1 = sa(m1); sa2 = sa(m2); sa3 = sa(m3)

Mu = unp.uarray([m1, m2, m3], sm); mu = unc.ufloat(m, sm)
au = g*(mu / Mu)

print("---\nPropEr A1 = {} +/- {}".format(a1, sa1))
print("Uncert A1 = {:.2u}".format(au[0]))
