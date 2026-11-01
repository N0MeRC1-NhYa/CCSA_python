def nieuw_kaartspel(c, v):
    return [color + value for color in c for value in v] 

def splits_kaartspel(c):
    return (c[:len(c) // 2], c[len(c) // 2:])

def faro_shuffle(s1, s2):
    a = []
    for i in range(min(len(s1), len(s2))):
        a.append(s1[i])
        a.append(s2[i])

    a.extend(s1[min(len(s1), len(s2)):])
    a.extend(s2[min(len(s1), len(s2)):])
    return a
