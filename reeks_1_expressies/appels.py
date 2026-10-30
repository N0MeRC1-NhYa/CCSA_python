box = 20
stack = 35
n = int(input())
print(n //( box * stack))
print((n % (box * stack)) // box)
print(n % box)