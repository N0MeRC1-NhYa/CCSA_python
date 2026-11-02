def letterfrequenties(str):
    letters = dict()
    for c in str.lower():
        if (c >= 'a' and c <= 'z'):
            if (c in letters.keys()):
                letters[c] += 1
            else:
                letters[c] = 1
    return letters

def letterposities(str):
    str= str.lower()
    posities = {letter : set() for letter in letterfrequenties(str).keys()}
    for k in posities.keys():
        print(k)
        for i in range(len(str)):
            if str[i] == k:
                posities[k].add(i)
    return posities
