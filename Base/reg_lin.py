#Regresión lineal sin término independiente
def reg_lin_b(x, y):
    print("---\nRegresión lineal sin término independiente\n---")

    n = len(x)

    sxy = (x*y).sum()
    sx2 = (x**2).sum()

    b = sxy / sx2

    sybx = ((y - b*x)**2).sum()
    s = (sybx / (n-1))**0.5
    sb = s / (sx2)**0.5

    sy2 = (y**2).sum()
    r = sxy / (sx2 * sy2)**0.5

    print("b=", b)
    print("s=", s, "sb=", sb)
    print("r=", r, "\n---")

    return (b, s, sb, r)

#Regresión lineal con término independiente
def reg_lin(x, y):
    print("---\nRegresión lineal con término independiente\n---")

    n = len(x)

    sx = x.sum()
    sy = y.sum()
    sxy = (x*y).sum()
    sx2 = (x**2).sum()
    sy2 = (y**2).sum()

    a = (sy*sx2 - sx*sxy) / (n*sx2 - sx**2)
    b = (n*sxy - sx*sy) / (n*sx2 - sx**2)

    sdesv = ((y - a - b*x)**2).sum()
    s = (sdesv/float(n-2))*0.5
    sa = s*(sx2 / (n*sx2 - sx**2))**0.5
    sb = s*(n / (n*sx2 - sx**2))**0.5

    r = (n*sxy - sx*sy)/(((n*sx2 - sx**2)*(n*sy2 - sy**2))**0.5)

    print("a=", a, "b=", b)
    print("s=", s, "sa=", sa, "sb=", sb)
    print("r=", r, "\n---")

    return (a, b, s, sa, sb, r)

#Regresión lineal ponderada con término independiente
def reg_lin_w(x, y, sy):
    print("---\nRegresión lineal ponderada con término independiente\n---")

    n = len(x)
    w = sy**(-2)

    sw = w.sum()
    swx = (w*x).sum()
    swy = (w*y).sum()
    swxy = (w*x*y).sum()
    swx2 = (w*x**2).sum()
    swy2 = (w*y**2).sum()
    det = sw * swx2 - swx**2

    a = (swy*swx2 - swx*swxy) / det
    b = (sw*swxy - swx*swy) / det

    sa = (swx2 / det)**0.5
    sb = (sw / det)**0.5

    swab = (w*(y - a - b*x)**2).sum()
    s = ((n / ((n-2) * sw)) * swab)**0.5

    r = (sw*swxy - swx*swy) / ((sw*swx2 - swx**2) * (sw*swy2 - swy**2))**0.5

    print("a=", a, "b=", b)
    print("s=", s, "sa=", sa, "sb=", sb)
    print("r=", r, "\n---")

    return (a, b, s, sa, sb, r)

#Regresión lineal ponderada sin término independiente
def reg_lin_wb(x, y, sy):
    print("---\nRegresión lineal ponderada sin término independiente\n---")

    n = len(x)
    w = sy**(-2)

    sw = w.sum()
    swx = (w*x).sum()
    swxy = (w*x*y).sum()
    swx2 = (w*x**2).sum()
    swy2 = (w*y**2).sum()

    b = swxy / swx2
    sb = 1 / (swx2)**0.5

    swb = (w*(y - b*x)**2).sum()
    s = ((n / ((n-1) * sw)) * swb)**0.5

    r = swxy / (swx2 * swy2)**0.5

    print("b=", b)
    print("s=", s, "sb=", sb)
    print("r=", r, "\n---")

    return (b, s, sb, r)
