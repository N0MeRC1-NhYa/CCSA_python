import math
def f(n):
    res = 0
    for i in range(1, n + 1):
        res += 1/(i ** 2)
    return res

def f_delta(d):
    res = 0
    i = 1
    while(abs(res - math.pi**2/6) > d):
        res += 1/(i ** 2)
        i+=1
    return i - 1

print(f(100))
print(f_delta(1/100))