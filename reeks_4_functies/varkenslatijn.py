import re
vowels = ['a', 'o', 'u', 'i', 'e', 'A', 'O', 'U', 'I', 'E']

def varkenswoord(str):
    if len(str) == 0:
        return ''
    cap = False
    if ((str[0] >= 'A' and str[0] <= 'Z') or str[0] in vowels):
        if str[0] in vowels:
            return str + "way"
        str = str[0].lower() + str[1:]
        cap = True
    j = 0
    tmp = ""
    while j < len(str) and str[j] not in vowels:
        tmp += str[j]
        if j + 1 < len(str) and str[j] == 'q' and str[j + 1] == 'u':
            tmp += 'u'
        j += 1
    if len(tmp) != 0 and tmp[-1] == 'u':
        j += 1 
    if cap:
        if j < len(str):
            str = str[:j] + str[j].upper() + str[j + 1:]
        else:
            tmp = tmp[0].upper() + tmp[1:]
    print(str[j:], str)
    return str[j:] + tmp + 'ay'

def varkenslatijn(line):
    return re.sub("[a-zA-Z]+",lambda m:varkenswoord(m.group(0)) , line)

