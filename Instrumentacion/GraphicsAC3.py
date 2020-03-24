import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Configure matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

fig, ax = plt.subplots()
fig.set_size_inches(w=5, h=2.5)
fig.patch.set_visible(False)
ax.axis('off')

#Curves
x = np.arange(0, 2 * np.pi, 0.1);
yg = 0.65 * np.cos(x)
yr = 0.65 * np.cos(x + (1/6) * np.pi)

plt.plot(x,yg, color="dodgerblue", zorder=2)
plt.plot(x,yr, color="tomato", zorder=2)

plt.text(np.pi * 0.5 - 0.2, 0.45, "$V_G$", fontsize=12, color="#1f77b4")
plt.text(np.pi * 0.5 - 0.5, -0.65, "$V_R$", fontsize=12, color="tomato")

#Intersecions
ig = (3/2) * np.pi
ir = (3/2) * np.pi - (1/6) * np.pi
yi = yv = np.arange(-0.85, 0.85, 0.1)
xi = np.ones(len(yi))

plt.scatter(ig, 0, color="dodgerblue", zorder=4)
plt.scatter(ir, 0, color="lightsalmon", zorder=4)

plt.plot(xi * ig, yi, color="skyblue", zorder=3)
plt.plot(xi * ir, yi, color="peachpuff", zorder=3)

plt.text(ig + 0.2, -0.8, "t1", fontsize=12, color="#1f77b4")
plt.text(ir - 0.5, -0.8, "t2", fontsize=12, color="tomato")

#Vertical Axis
yv = np.arange(-1, 1, 0.1)
xv = np.zeros(len(yv))
plt.plot(xv, yv, color="black", zorder=0, linewidth=0.3)
#Horizontal Axis
xh = np.arange(0, 2 * np.pi, 0.2)
yh = np.zeros(len(xh))
plt.plot(xh, yh, color="black", zorder=0, linewidth=0.3)
plt.text(1.95 * np.pi, -0.2, "t", fontsize=12, color="black")

#m, b = np.polyfit(x, y, 1)
#plt.plot(x, m*x + b, zorder=1, color="skyblue")
#x2 = (1 - b)/m
#plt.scatter(x2, 1, zorder=3, color="tomato")
#print("Frecuencia corte:", x2)

#plt.title('Voltaje (V) frente a intensidad (I)')
plt.savefig("Osciloscope1.pgf", bbox_inches = "tight")
