akkorden = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def ontleding(s):
    if s in akkorden:
        return (s, '')
    i = 0
    while i < len(s):
        i += 1
        if s[:i] not in akkorden:
            break
    return (s[:i - 1], s[i - 1:])

def noten(ak, delta):
    res = []
    for i in delta:
        res.append(akkorden[(akkorden.index(ak) + i) % (len(akkorden))])
    return res

def akkoord(ak, types, sym):
    akkord, typ = ontleding(ak) 
    return tuple(noten(akkord,types.get(sym.get(typ))))