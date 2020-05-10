import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_w as rl
import mpl_config as mpl

D = [pd.read_csv("CC-{}.csv".format(i), sep=';', decimal=',') for i in range(1,4)]

I = np.asarray([[D[j]["I{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])
T = np.asarray([[D[j]["T{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])
LnI = np.asarray([[D[j]["LnI{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])
sLnI = np.asarray([[D[j]["sLnI{}".format(i)].to_numpy() for i in range(1,5)] for j in range(0,3)])

#Selector de experimento
exp = 1 #Número de experiencia (0-2)
rep = 3 #Número de repetición (0-3)

#Regresión lineal ponderada
x = T[exp,rep][~np.isnan(T[exp,rep])]
y = LnI[exp,rep][~np.isnan(LnI[exp,rep])]

sy = sLnI[exp,rep][~np.isnan(sLnI[exp,rep])]

a, b = rl(x,y,sy)[0:2]

xr = np.linspace(min(x), max(x), 20)
yr = a + b*xr

#Gráficas
plt.scatter(T[exp,rep], np.log(I[exp,rep]))
plt.plot(xr, yr)
