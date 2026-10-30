sum = 0
val = -1
while sum < 21 and val != 0:
    val = int(input())
    sum += val
if sum == 21:
    print("Gewonnen!")
elif sum > 21:
    print(f"Verbrand ({sum})")
else:
    print(f"Voorzichtig gespeeld ({sum})")