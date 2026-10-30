def lazy_solve(r_w, w_b, s):
    for r in range(2, r_w):
        for w in range(2, w_b):
            for b in range(2, w_b):
                if w + b == w_b and r + w == r_w and (s == "<" and r + b < w_b or s == ">" and r + b > w_b):
                    return [b, w, r]
    return None

r_w = int(input())
w_b = int(input())
symbol = input()
print(*lazy_solve(r_w, w_b, symbol), sep="\n")