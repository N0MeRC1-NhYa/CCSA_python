def ggd(a, b):
    return abs(a) if b == 0 else ggd(b, a % b) 