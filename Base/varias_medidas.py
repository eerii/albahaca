def tratamiento_datos(x, sb=0):
    import numpy as np
    #Media
    fmed = lambda x: x.sum() / len(x)
    med = fmed(x)

    #Desviación típica muestra
    fsa = lambda x, m: (((x - m)**2).sum() / (len(x) - 1))**0.5
    sa = fsa(x, med)

    #Valores discordantes
    k = 2
    lb = med - k*sa
    ub = med + k*sa
    e = np.array(np.where(np.logical_or(x <= lb, x >= ub))).flatten().astype(np.int32).tolist()

    #Eliminar valores y calcular de nuevo
    nx = np.delete(x, e)
    med = fmed(nx)
    sa = fsa(nx, med)

    #Desviación típica media
    sm = sa / len(nx)**0.5

    #Incertidumbre combinada
    sc = (sm**2 + sb**2)**0.5

    print("---\nTratamiento de datos\n---")
    print("Media: {}, sa: {}, sb: {}, sc: {}".format(med, sa, sb, sc))
    if len(e) > 0:
        print("Eliminados: {}".format(x[e]))
        print("Indices: {}\n---".format(e))

    return nx, med, sc, e
