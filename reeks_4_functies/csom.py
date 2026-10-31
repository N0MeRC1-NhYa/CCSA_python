def csom(n):
    if n <= 9:
        return n
    sum = 0
    for i in str(n):
        sum += int(i)
    return csom(sum)