import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Constantes
pm = 4 * np.pi * 10**(-7)
i = 2.55
n = 154
r = 0.2

#Calculo campo magnético
B = lambda pm, i, n, r, a, z: ((pm * i * n) / (2 * r)) * ((1 / (1 + ((z - (a/2)) / (r))**2)**(3/2)) + (1 / (1 + ((z + (a/2)) / (r))**2)**(3/2)))

#Leer datos
d1 = pd.read_csv("BH-1.csv", sep=';', decimal=',')
z1 = d1["z"]
Be1 = d1["Bexp"]
d2 = pd.read_csv("BH-2.csv", sep=';', decimal=',')
z2 = d2["z"]
Be2 = d2["Bexp"]
d3 = pd.read_csv("BH-3.csv", sep=';', decimal=',')
z3 = d3["z"]
Be3 = d3["Bexp"]

#Curvas teóricas
z = np.linspace(-0.450, 0.450, 450)
Bt1 = B(pm, i, n, r, r, z)
Bt2 = B(pm, i, n, r, r/2, z)
Bt3 = B(pm, i, n, r, 2*r, z)

#Gráficas
plt.plot(z,Bt1,color="limegreen")
plt.plot(z,Bt2,color="dodgerblue")
plt.plot(z,Bt3,color="tomato")

plt.scatter(z1,Be1,color="lightgreen")
plt.scatter(z2,Be2,color="skyblue")
plt.scatter(z3,Be3,color="lightsalmon")

#Desviación típica
s = lambda Be, Bt: (1/len(Be)) * (np.sum(((Be - Bt)**2).to_numpy()))**0.5
s1 = s(Be1, B(pm, i, n, r, r, z1))
s2 = s(Be2, B(pm, i, n, r, r, z2))
s3 = s(Be3, B(pm, i, n, r, r, z3))

print("Desviaciones - s1: {}, s2: {}, s3: {}".format(s1, s2, s3))

plt.show()
