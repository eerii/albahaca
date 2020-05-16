import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import uncertainties as unc

import sys
sys.path.insert(1, '../Base')
from varias_medidas import tratamiento_datos as tdatos
import mpl_config as mpl

#Datos
sb = 0.001 * 2
D = 0.02167
sD = 0.00048

d = pd.read_csv("MI2_Cuerpos.csv", sep=';', decimal=',')
td = d["stDisco"].to_numpy() * 2
tc = d["stCil"].to_numpy() * 2

#DISCO
print("---\nDisco\n---")

Td, sTd = tdatos(td, sb)

#Momento Inercia Experimental
Id = (Td**2 * D) / (4*np.pi**2)

#Propagación Incertidumbres
sId = ((((Td*D) / (2*np.pi**2))**2 * sTd**2) + ((Td**2 / (4*np.pi**2))**2 * sD**2))**0.5
#Tdu = unc.ufloat(Td, sTd); Du = unc.ufloat(D, sD); Iu = (Tdu**2 * Du) / (4*np.pi**2)

#Momento Inercia Teórico
Md = 0.2959
sMd = 0.00001
Rd = 0.108
sRd = 0.001
Idt = (Md * Rd**2) / 2

#Propagación Incertidumbres
sIdt = (((Rd**2 / 2)**2 * sMd**2) + ((Md * Rd)**2 * sRd**2))**0.5
#Mdu = unc.ufloat(Md, sMd); Rdu = unc.ufloat(Rd, sRd); Idu = (Mdu * Rdu**2) / 2

print("I(exp) = {} +/- {}".format(Id, sId))
print("I(teo) = {} +/- {}".format(Idt, sIdt))


#CILINDRO
print("---\nCilindro\n---")

Tc, sTc = tdatos(tc, sb)

#Momento Inercia Experimental
Ic = (Tc**2 * D) / (4*np.pi**2)

#Propagación Incertidumbres
sIc = ((((Tc*D) / (2*np.pi**2))**2 * sTc**2) + ((Tc**2 / (4*np.pi**2))**2 * sD**2))**0.5

#Momento Inercia Teórico
Mc = 0.3731
sMc = 0.00001
Rc = 0.05
sRc = 0.001
Ict = (Mc * Rc**2) / 2

#Propagación Incertidumbres
sIct = (((Rc**2 / 2)**2 * sMc**2) + ((Mc * Rc)**2 * sRc**2))**0.5
#Mdu = unc.ufloat(Md, sMd); Rdu = unc.ufloat(Rd, sRd); Idu = (Mdu * Rdu**2) / 2

print("I(exp) = {} +/- {}".format(Ic, sIc))
print("I(teo) = {} +/- {}".format(Ict, sIct))
