x = int(input())
if x % 2 == 1:
    odd_cnt = 1
else:
    odd_cnt = 0
for i in range(2, x // 2 + 1):
    if x % i == 0 and i % 2 != 0:
        odd_cnt += 1
print(odd_cnt)