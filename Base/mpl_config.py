def inicio(c, s=[5.0, 3.5]):
    import matplotlib
    from cycler import cycler

    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "pdflatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
        'figure.figsize': s,
        'scatter.edgecolors': "black"
    })

    ccycler = 0
    if c <= 2:
        ccycler = (cycler(color=["royalblue", "indianred"]))
    if c == 3:
        ccycler = (cycler(color=["royalblue", "mediumseagreen", "tomato"]))
    if c >= 4:
        ccycler = (cycler(color=["royalblue", "mediumseagreen", "sandybrown", "tomato", "orchid"]))
    matplotlib.rcParams['axes.prop_cycle'] = ccycler

def guardar(n, xl, yl, leg=True, lab=True):
    import matplotlib.pyplot as plt
    if lab:
        plt.xlabel(xl)
        plt.ylabel(yl, rotation=0, labelpad=20)
    if leg: plt.legend()
    plt.savefig(n + ".pgf", bbox_inches = "tight")
