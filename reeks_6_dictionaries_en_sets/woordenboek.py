def vertaling_toevoegen(k, v, w):
    if k not in w.keys():
        w[k] = v

def vertaling(v, w):
    if v in w.keys():
        return w.get(v)
    return '???'