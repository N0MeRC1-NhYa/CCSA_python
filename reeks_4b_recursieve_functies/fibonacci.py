def fib(n):
    # if (n == 0):
    #     return 0
    # if (n == 1 or n == 2):
    #     return 1
    # return fib(n - 1) + fib(n - 2)
    a = [0, 1, 1]
    while len(a) <= n:
        a.append(a[-2] + a[-1])
    return a[n]