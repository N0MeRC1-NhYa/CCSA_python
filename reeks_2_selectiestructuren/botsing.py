def dot_inside(s, d):
    return d[0] > min(s[0], s[2]) and d[0] < max(s[2], s[0]) and d[1] > min(s[1], s[3]) and d[1] < max(s[1], s[3])

def dot_border(s, d):
    return ((d[0] == s[0] or d[0] == s[2]) and (d[1] >= min(s[1], s[3]) and d[1] <= max(s[1], s[3]))) or \
            ((d[1] == s[1] or d[1] == s[3]) and (d[0] >= min(s[0], s[2]) and d[0] <= max(s[0], s[2])))

data = []
for i in range(8):
    data.append(int(input()))

square = data[:4]
dots = [[data[4], data[5]],
        [data[4], data[7]],
        [data[6], data[7]],
        [data[6], data[5]]]

cnt_in = 0
cnt_br = 0
for d in dots:
    if dot_inside(square, d):
        cnt_in += 1
    if dot_border(square, d):
        cnt_br += 1
        
if cnt_in == 0 and cnt_br < 4: 
    print("geen botsing")
else:                           # if any dot of square2 is inside square1 or if square2 is exactly square1(???)
    print("botsing")