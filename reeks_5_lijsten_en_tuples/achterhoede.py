def zien(t):
    a = []
    r_cnt = 0
    for i in range(len(t)):
        a.append('B' if r_cnt % 2 == 0 else 'R')
        if (t[i] == 'R'):
            r_cnt += 1
    return tuple(a)

def zeggen(t):
    transform = {'R' : 'B', 'B' : 'R'}
    a = []
    r_cnt = 0
    for i in range(len(t) - 1, -1, -1):
        a.append(t[i] if r_cnt % 2 == 0 else transform[t[i]])
        if (a[-1] == 'R'):
            r_cnt += 1
    a.reverse()
    return tuple(a)