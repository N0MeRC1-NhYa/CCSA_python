def driehoek(r):
    if type(r) is not int or r < 0:
        raise AssertionError("ongeldig aantal rijen")
    res = []
    for i in range(1, r + 1):
        tmp = [1] * i
        for j in range(1, i - 1):
            tmp[j] = res[-1][j - 1] + res[-1][j] 
        res.append(tmp)
    return res

def zeshoek(r, k):
    if type(r) is not int or type(k) is not int or k >= r or k <= 1:
        raise AssertionError("ongeldige interne positie")
    dr = driehoek(r + 1)
    return [dr[r - 2][k - 2], dr[r - 2][k - 1], dr[r - 1][k], dr[r][k], dr[r][k - 1], dr[r - 1][k - 2]]

def kwadraat(r, k):
    res = 1
    zes = zeshoek(r, k)
    for i in zes:
        res *= i
    sqr = int(res ** 0.5)
    return "{} x {} x {} x {} x {} x {} = {} = {} x {}".format(*zes, res, sqr, sqr)
