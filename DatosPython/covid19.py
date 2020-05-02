import numpy as np
import matplotlib.pyplot as plt

nome = "serie_historica_acumulados.csv"

ficheiro = open(nome, "r").read()
datos = ficheiro.split("\n")

datos[1:-5]

DATOS = []
for i in datos[1:-5]:
    DATOS.append(i.split(","))

DATOS = np.array(DATOS)

GA = DATOS[DATOS[:, 0] == "GA"]
float(GA[:,-1][20])

recuperados = []
for i in GA[:, -1]:
    if i == "":
        recuperados.append(0)
    else:
        recuperados.append(float(i))
recuperados = np.array(recuperados)

uci = []
for i in GA[:, -3]:
    if i == "":
        uci.append(0)
    else:
        uci.append(float(i))
uci = np.array(uci)

casos = []
for i in GA[:, 2]:
    if i == "":
        casos.append(0)
    else:
        casos.append(float(i))
casos = np.array(casos)
casos
nuevos_casos = casos[1:] - casos[:-1]

datas = []
for i in GA[:,1]:
    d, m, a = i.split("/")
    if len(d) < 2:
        d = "0" + d
    if len(m) < 2:
        m = "0" + m
    datas.append(np.datetime64(a + "-" + m + "-" + d))
datas = np.array(datas)

fig, ax = plt.subplots(2, 2)
ax[0,0].plot(datas, casos)
ax[1,0].bar(datas[1:], nuevos_casos)
ax[0,1].plot(datas, recuperados, "o")
ax[1,1].plot(datas, uci, "o")
