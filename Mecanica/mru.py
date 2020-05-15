import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import uncertainties as unc

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_b as rl
from varias_medidas import tratamiento_datos as tdatos
import mpl_config as mpl

mpl.inicio(3, [3, 2.2])

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

c = ["royalblue", "mediumseagreen", "tomato"]

#Gráficas
for i in range(len(T)):
    plt.clf()
    plt.scatter(T[i], S[i], color=c[i], edgecolors="black", linewidth=0.5)

    #Ajuste
    b = rl(T[i], S[i])[0]
    xr = np.linspace(min(T[i]), max(T[i]), 10)
    yr = b*xr
    #plt.plot(xr, yr, color=c[i])

    #mpl.guardar("LN_MRU_{}".format(i+1), "T(s)", "S(m)", False)

    #Tratamiento Datos
    print("T1 - ", i+1)
    mT1, sT1 = tdatos(T1[i], st)
    print("T2 - ", i+1)
    mT2, sT2 = tdatos(T2[i], st)

    #Velocidades instantáneas
    V1 = L / mT1
    V2 = L / mT2

    sV1 = ((sl**2 / mT1**2) + ((L**2 * st**2) / mT1**4))**0.5
    sV2 = ((sl**2 / mT2**2) + ((L**2 * st**2) / mT2**4))**0.5

    Lu = unc.ufloat(L, sl); T1u = unc.ufloat(mT1, st); T2u = unc.ufloat(mT2, st)
    V1u = Lu / T1u; V2u = Lu / T2u

    #print("---\nPropEr V1 = {} +/- {}".format(V1, sV1))
    print("V1 = {:.2u}".format(V1u))
    print("V2 = {:.2u}".format(V2u))
