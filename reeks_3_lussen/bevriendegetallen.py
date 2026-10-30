x = int(input())
y = int(input())
som_x = 0
som_y = 0
for i in range(1, max(x, y) // 2 + 1):
    if x % i == 0:
        som_x += i
    if y % i == 0:
        som_y += i
if som_x == y and som_y == x:
    print(f"{x} en {y} zijn bevriende getallen")
else:
    print(f"{x} en {y} zijn geen bevriende getallen")
