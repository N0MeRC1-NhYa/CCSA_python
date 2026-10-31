rot_dig = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
def bovensteboven(n):
    res = ""
    for s in str(n)[::-1]:
        if s not in rot_dig.keys():
            return False
        res += rot_dig.get(s)
    return res == str(n)

def volgende(n):
    i = n + 1
    while not bovensteboven(i):
        i+=1
    return i