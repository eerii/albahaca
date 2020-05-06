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

    a = (sy*sx2 - sx*sxy) / (n*sx2 - sx**2)
    b = (n*sxy - sx*sy) / (n*sx2 - sx**2)

    sdesv = ((y - a - b*x)**2).sum()
    s = (sdesv/float(n-2))*0.5
    sa = s*(sx2 / (n*sx2 - sx**2))**0.5
    sb = s*(n / (n*sx2 - sx**2))**0.5

    sy2 = (y**2).sum()
    r = (n*sxy - sx*sy)/(((n*sx2 - sx**2)*(n*sy2 - sy**2))**0.5)

    print("a=", a, "b=", b)
    print("s=", s, "sa=", sa, "sb=", sb)
    print("r=", r, "\n---")

    return (a, b, s, sa, sb, r)
