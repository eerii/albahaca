def inicio():
    import matplotlib

    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "pdflatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })

def figure():
    import matplotlib.pyplot as plt
    fig = plt.figure()
    fig.set_size_inches(w=5, h=3.5)
    return fig

def guardar(n, xl, yl):
    import matplotlib.pyplot as plt
    plt.xlabel(xl)
    plt.ylabel(yl, rotation=0, labelpad=20)
    plt.savefig(n + ".pdf", bbox_inches = "tight")
