import math
def zeef(n):
    if n < 2:
        return None
    a = [i for i in range(1, n + 1)]
    i = 0
    for i in range(2, math.ceil(n ** 0.5) + 1):
        if a[i - 1] != 0:
            j = i - 1 + i
            while j < n:
                a[j] = 0
                j += i
    ar = []
    for i in range(1, n):
        if (a[i] != 0):
            ar.append(a[i])
    return ar


