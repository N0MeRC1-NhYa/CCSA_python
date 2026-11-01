def iszigzag(a):
    for i in range(1, len(a) - 1):
        if i % 2 == 1 and (a[i - 1] < a[i] or a[i] > a[i + 1]):
            return False
        if i % 2 == 0 and (a[i - 1] > a[i] or a[i] < a[i + 1]):
            return False
    if len(a) == 2 and a[0] < a[1]:
        return False
    return True

def zigzag_traag(a):
    a.sort()
    for i in range(0, len(a) - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]
    return a

def zigzag_snel(a):
    for i in range(0, len(a), 2):
        if i - 1 > 0 and a[i - 1] > a[i]:
            a[i - 1], a[i] = a[i], a[i - 1]
        if i + 1 < len(a) and a[i + 1] > a[i]:
            a[i + 1], a[i] = a[i], a[i + 1]
    return a
        