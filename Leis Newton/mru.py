import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import uncertainties as unc

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_b as rl
from varias_medidas import tratamiento_datos as tdatos
import mpl_config as mpl

#Datos
m1 = 0.20089
m2 = 0.26079
m3 = 0.30167
L = 0.1 #Diafragma

sm = 0.00001
st = 0.001
sl = 0.001

d = [pd.read_csv("LN_MRU_M{}.csv".format(i), sep=';', decimal=',') for i in range(1,4)]
S = np.array([d[j]["S"] for j in range(0,3)])
T = np.array([d[j]["T"] for j in range(0,3)])
T1 = np.array([d[j]["T1"] for j in range(0,3)])
T2 = np.array([d[j]["T2"] for j in range(0,3)])

#Gráficas
plt.scatter(T[0], S[0])

#Ajuste
b = rl(T[0], S[0])[0]
xr = np.linspace(min(T[0]), max(T[0]), 10)
yr = b*xr
plt.plot(xr, yr)

#Tratamiento Datos
T1, sT1 = tdatos(T1[0], st)
T2, sT2 = tdatos(T2[0], st)

#Velocidades instantáneas
V1 = L / T1
V2 = L / T2

sV1 = ((sl**2 / T1**2) + ((L**2 * st**2) / T1**4))**0.5
sV2 = ((sl**2 / T2**2) + ((L**2 * st**2) / T2**4))**0.5

Lu = unc.ufloat(L, sl); T1u = unc.ufloat(T1, st); T2u = unc.ufloat(T2, st)
V1u = Lu / T1u; V2u = Lu / T2u

print("---\nPropEr V1 = {} +/- {}".format(V1, sV1))
print("Uncert V1 = {:.2u}".format(V1u))
