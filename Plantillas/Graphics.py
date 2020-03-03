import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#Configure matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

#Read from CSV to pandas dataframe
d = pd.read_csv("sealevel.csv")
print(d)
year = d["YEAR"]
sea_levels = d["SEA LEVEL"]

#Scatter Plot
fig = plt.figure()
fig.set_size_inches(w=4.7747, h=3.5)
plt.scatter(year, sea_levels)
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sealevel')
#plt.show()

#Save the figure
plt.savefig('sealevel.pgf')
