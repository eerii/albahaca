import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_b as rl
import mpl_config as mpl

#Datos
d = pd.read_csv("MI1_PhiF.csv", sep=';', decimal=',')
phi = d["PhiRad"]
M = d["M"]

#Regresión lineal sin término independiente
b, sb = rl(phi, M)[0:3:2]
xr = np.linspace(min(phi), max(phi), 10)
yr = b*xr

#Gráficas
plt.scatter(phi,M)
plt.plot(xr, yr)
