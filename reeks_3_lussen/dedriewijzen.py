def lazy_solve(n):
    for a in range(1, n):
        for b in range(1, n - a):
            c = n - a - b
            if a * b * c == n * 10000:
                return [a / 100, b / 100, c / 100]
    return None

x = input().split(".")
while len(x[1]) < 2:
    x[1] = f"{x[1]}{0}"
x = int("".join(x))
ans = lazy_solve(x)
print("€{:.2f} + €{:.2f} + €{:.2f} = €{:.2f} x €{:.2f} x €{:.2f} = €{:.2f}".format(*ans, *ans, x / 100))
