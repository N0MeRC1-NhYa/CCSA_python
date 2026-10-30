som = 0
for i in range(1, 10):
    som += i * int(input())
if (som % 11 == int(input())):
    print("OK")
else:
    print("FOUT")