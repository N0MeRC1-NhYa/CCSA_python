def even_oneven(n):
    e = 0
    o = 0
    for i in str(n):
        if int(i) % 2 == 0:
            e += 1
        else:
            o += 1
    return (e, o)

def volgende(n):
    e, o = even_oneven(n)
    return int(f"{e}{o}{e + o}")

def stappen(n):
    cnt = 0
    while n != 123:
        cnt += 1
        n = volgende(n)
    return cnt