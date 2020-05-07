import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '../Base')
from varias_medidas import tratamiento_datos as tdatos
import mpl_config as mpl

#Datos
d = pd.read_csv("MI2_Cuerpos.csv", sep=';', decimal=',')
td = d["TDisco"].to_numpy()
sb = 0.001
x, m, sc, e = tdatos(td, sb)
