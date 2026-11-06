def beweeg(pos, dir):
    x, y = pos
    if dir == '<':
        x -= 1
    elif dir == '>':
        x += 1
    elif dir == '^':
        y += 1
    elif dir == 'v':
        y -= 1
    return (x, y)

def teruggekeerd(but):
    s = (0, 0)
    e = (0, 0)
    for nav in but:
        e = beweeg(e, nav)
    return s == e 

def laatste_levende_positie(but):
    s = (0, 0)
    e = (0, 0)
    b_cnt = 0
    for i in range(len(but)):
        if i > 0 and teruggekeerd([but[i - 1], but[i]]):
            break
        e = beweeg(e, but[i])
        b_cnt += 1
    return (b_cnt, s[0] + e[0], s[1] + e[1])