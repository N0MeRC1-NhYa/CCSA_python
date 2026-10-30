def count_mins_between(h1, m1, h2, m2):
    return (h2 - h1) * 60 + m2 - m1

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
if h1 < 18 or h2 < h1 or (h2 == h1 and m2 < m1) or (h2 == 0 and m2 > 0):
    print("ongeldige invoer")
else:
    if h2 <= 21 and m2 <= 30:
        print(count_mins_between(h1, m1, h2, m2) / 30)
    elif h1 > 21 or (h1 == 21 and m1 > 30): 
        print(count_mins_between(h1, m1, h2, m2) / 15)
    else:
        print(count_mins_between(h1, m1, 21, 30) / 30 + count_mins_between(21, 30, h2, m2) / 15)
