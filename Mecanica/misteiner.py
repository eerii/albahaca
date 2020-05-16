import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp

import sys
sys.path.insert(1, '../Base')
from varias_medidas import tratamiento_datos as tdatos
from reg_lin import reg_lin as rl
import mpl_config as mpl

mpl.inicio(1)

#CONSTANTES GLOBALES
D = 0.02167
sD = 0.00048
sb = 0.001 * 2

#FUNCIONES
def m_inercia_exp(d):
    #Tratamiento Datos
    T = np.zeros(len(d))
    sT = np.zeros(len(d))

    for i in range(len(d)):
        T[i], sT[i] = tdatos(d[i], sb)
        print("---\nT{} = {:.2u}".format(i*3, unc.ufloat(T[i], sT[i])))

    #Momento Inercia
    I = (T**2 * D) / (4*np.pi**2)

    #Propagación Incertidumbres
    sI = ((((T*D) / (2*np.pi**2))**2 * sT**2) + ((T**2 / (4*np.pi**2))**2 * sD**2))**0.5

    Tu = unp.uarray(T, sT); Du = unc.ufloat(D, sD); Iu = (Tu**2 * Du) / (4*np.pi**2)

    print("---")
    for i in range(len(I)):
        #print("PropEr I{} = {} +/- {}".format(i*3, I[i], sI[i]))
        print("I{} = {:.2u}\n---".format(i*3, Iu[i]))

    return I

def m_inercia_steiner(M, sM, R, sR, It, sIt, dist):
    #Steiner
    Is = []; sIs = []; Isu = unp.uarray([0 for i in range(len(I))], [0 for i in range(len(I))])

    distu = unp.uarray(dist, [sR for i in range(len(dist))])
    for i in range(len(dist)):
        Is.append(It + M * (dist[i])**2)
        sIs.append(((sIt**2) + ((dist[i])**4 * sM**2) + ((2*(dist[i])*M)**2 * sR**2))**0.5)

        Isu[i] = Itu + Mu * (distu[i])**2

        #print("PropEr Is{} = {} +/- {}".format(i*3, Is[i], sIs[i]))
        print("Is{} = {:.2u}\n---".format(i*3, Isu[i]))

def graph(d, I,n):
    plt.clf()
    #Representación
    x = d**2
    y = I

    plt.scatter(x, y)

    #Regresión Lineal
    a, b = rl(x, y)[0:2]
    xr = np.linspace(min(x), max(x), 20)
    yr = a + b * xr

    plt.plot(xr, yr)
    mpl.guardar("MI3_Steiner_{}".format(n), "$d^2 (m^2)$", "$I (kg \\cdot m^2)$", False)


#DISCO
print("---\nDisco\n---")

M = 0.3974
sM = 0.00001
R = 0.15
sR = 0.001

dist = np.array([0.03*i for i in range(5)])

#Cargar CSV
dcsv = pd.read_csv("MI3_Steiner_Disco.csv", sep=';', decimal=',')
d = [dcsv["0,0{}".format(i)].to_numpy() for i in range(0,10,3)]; d.append(dcsv["0,12"].to_numpy()); d = np.array(d); d *= 2 #Periodo completo

#Inercia Teórica
It = (M * R**2) / 2
sIt = (((R**2 / 2)**2 * sM**2) + ((M * R)**2 * sR**2))**0.5

Mu = unc.ufloat(M, sM); Ru = unc.ufloat(R, sR); Itu = (Mu * Ru**2) / 2

print("It = {:.2u}\n---".format(Itu))

#Llamar Funciones
I = m_inercia_exp(d)
m_inercia_steiner(M, sM, R, sR, It, sIt, dist)
graph(dist, I, "Disco")


#BARRA
print("---\nBarra\n---")

M = 0.13172
sM = 0.00001
L = 0.60
sL = 0.001

dist = np.array([0.03*i for i in range(10)])

#Cargar CSV
dcsv = pd.read_csv("MI3_Steiner_Barra.csv", sep=';', decimal=',')
d = []
for i in range(len(dist)):
    ind = str(dist[i]).replace(".", ",")
    if len(ind) == 3: ind = ind + "0"
    d.append(dcsv[ind])
d = np.array(d) * 2 #Periodo completo

#Inercia Teórica
It = (M * L**2) / 12
sIt = (((L**2 / 12)**2 * sM**2) + (((M*L) / 6)**2 * sL**2))**0.5

Mu = unc.ufloat(M, sM); Lu = unc.ufloat(L, sL); Itu = (Mu * Lu**2) / 12

print("It = {:.2u}\n---".format(Itu))

#Llamar Funciones
I = m_inercia_exp(d)
m_inercia_steiner(M, sM, L, sL, It, sIt, dist)
#graph(dist, I, "Barra")
