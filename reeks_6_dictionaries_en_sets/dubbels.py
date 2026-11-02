def dubbel(l):
    nums = set()
    for i in l:
        if i in nums:
            return i
        else:
            nums.add(i)
    return None

def dubbels(l):
    uniq = set()
    dubbel = set()
    for i in l:
        if i not in uniq and i not in dubbel:
            uniq.add(i)
        elif i in uniq:
            dubbel.add(i)
            uniq.remove(i)
    return (uniq, dubbel) 