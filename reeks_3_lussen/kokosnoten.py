p, n = int(input()), int(input())

for i in range(1, p + 1):
    take_p = n // p
    take_a = n % p
    print(f"{n if n != 0 else "geen"} {"noten" if n != 1 else "noot"} = {take_p if take_p != 0 else "geen"} {"noten" if take_p != 1 else "noot"} voor piraat#{i} en {take_a if take_a != 0 else "geen"} {"noten" if take_a != 1 else "noot"} voor de aap")
    n -= take_p + take_a
print(f"elke piraat krijgt {n // p if n // p != 0 else "geen"} {"noten" if n // p != 1 else "noot"} en {n % p if n % p != 0 else "geen"} {"noten" if n % p != 1 else "noot"} voor de aap")
