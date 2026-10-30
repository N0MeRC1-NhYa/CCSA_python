a = float(input())
b = float(input())
c = float(input())
D = b * b - 4 * a * c
if D < 0:
    print("geen wortels")
elif D == 0:
    print("een wortel")
    print(-b / (2 * a))
else:
    print("twee wortels")
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)
    if x1 > x2:
        print(x2, x1, sep="\n")
    else:
        print(x1, x2, sep="\n")
    
   