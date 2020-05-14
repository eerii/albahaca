import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_w as rl
import mpl_config as mpl

mpl.inicio(4)#, [7., 5.])

D = [pd.read_csv("CC-{}.csv".format(i), sep=';', decimal=',') for i in range(1,4)]

I = np.asarray([[D[j]["I{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])
T = np.asarray([[D[j]["T{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])
LnI = np.asarray([[D[j]["LnI{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])
sLnI = np.asarray([[D[j]["sLnI{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])

#Selector de experimento
exp = 2 #Número de experiencia (0-2)
rep = 3 #Número de repetición (0-3)

c = ["royalblue", "mediumseagreen", "sandybrown", "tomato"]

for r in range(4):
    x = T[exp,r][~np.isnan(T[exp,r])]
    y = LnI[exp,r][~np.isnan(LnI[exp,r])]
    sy = sLnI[exp,r][~np.isnan(sLnI[exp,r])]

    a, b = rl(x,y,sy)[0:2]

    xr = np.linspace(min(x), max(x), 20)
    yr = a + b*xr

    plt.scatter(x, y, linewidth=0.5, label='$C_{}$'.format(r+1))
    plt.plot(xr, yr)

#Regresión lineal ponderada y gráficas
"""fig, axs = plt.subplots(2, 2)
for r in range(4):
    x = T[exp,r][~np.isnan(T[exp,r])]
    y = LnI[exp,r][~np.isnan(LnI[exp,r])]
    sy = sLnI[exp,r][~np.isnan(sLnI[exp,r])]

    a, b = rl(x,y,sy)[0:2]

    xr = np.linspace(min(x), max(x), 20)
    yr = a + b*xr

    yi = 1 if r%2 == 1 else 0
    xi = 0 if r < 2 else 1

    axs[xi, yi].scatter(x, y, color=c[r], edgecolors="black", linewidth=0.5)
    axs[xi, yi].plot(xr, yr, color=c[r])
    axs[xi, yi].set_title('$C_{}$'.format(r+1))

for ax in axs.flat:
    ax.set(xlabel='T(s)', ylabel='$\ln{I}(A)$')
    ax.label_outer()"""

mpl.guardar("CC-3LR", "T(s)", "$\ln{I}(A)$")#, False, False)

import uncertainties as unc
from uncertainties.umath import *
v = unc.ufloat(10.2, 0.1)
c = unc.ufloat(10**(-5), 0.05*10**(-5))
r = unc.ufloat(4.4*10**6, 0.05*4.4*10**6)
a = log(v/r)
b = (-1)/(r*c)
print("a = {:.2u}, b = {:.2u}".format(a, b))
