def eerste(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                return (i, j)

def opvolger(m, x, y):
    for i in range(max(x - 1, 0), min(x + 1, len(m) - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, len(m[i]) - 1) + 1):
            if m[x][y] == m[i][j] - 1:
                return (i, j)
    return (None, None)

def laatste(m):
    ind = eerste(m)
    prev = ind
    while (ind[0] is not None):
        prev = ind
        ind = opvolger(m, *ind)
    return prev

def hidato(m):
    i, j = laatste(m)
    return m[i][j] == len(m) * len(m[0]) 
