def omgekeerd(d):
    res = dict.fromkeys(d.values())
    for k in d.keys():
        res[d.get(k)] = k
    return res

def code39(str, d):
    res = ""
    for i in str.upper():
        res += d.get(i) + 's'
    return res[:-1]

def decode39(str, d):
    res = ""
    dec = omgekeerd(d)
    for i in range(0, len(str), 10):
        res += dec.get(str[i:i+9])
    return res        