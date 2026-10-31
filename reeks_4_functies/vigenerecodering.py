import math

def codeer(m, w):
    w_line = w * math.ceil(len(m) / len(w))
    res = ""
    for i in range(len(m)):
        if ord(m[i]) >= ord("A") and ord(m[i]) <= ord("Z"):
            res += chr(ord("A") + ( ord(m[i]) + ord(w_line[i]) - 2 * ord("A")) % 26)
        else:
            res += m[i]
    return res

def decodeer(m, w):
    w_line = w * math.ceil(len(m) / len(w))
    res = ""
    for i in range(len(m)):
        if ord(m[i]) >= ord("A") and ord(m[i]) <= ord("Z"):
            res += chr(ord("A") + ( ord(m[i]) - ord(w_line[i]) - 2 * ord("A")) % 26)
        else:
            res += m[i]
    return res