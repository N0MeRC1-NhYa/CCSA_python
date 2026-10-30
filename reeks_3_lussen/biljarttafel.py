def in_hole(b, c):
    return c in b

def define_side(b, c):
    if c[0] == 0:
        return "linkerband"
    if c[1] == 0:
        return "onderband"
    if c[0] == b[3][0]:
        return "rechterband"
    return "bovenband"

def define_hole(b, c):
    return ["linkeronderpocket", "linkerbovenpocket", "rechteronderpocket",  "rechterbovenpocket"][b.index(c)]

def shoot(board, lim_x, lim_y):
    cur_coor = [0, 0]
    x_dir = -1
    y_dir = -1
    while True: #  not in_hole(board, cur_coor)
        if lim_x == cur_coor[0]:
            d_x = lim_x
            x_dir = -1
        else:
            if cur_coor[0] == 0:
                x_dir = 1
            if x_dir == -1:
                d_x = cur_coor[0]
            else:
                d_x = lim_x - cur_coor[0]

        if lim_y == cur_coor[1]:
            d_y = lim_y
            y_dir = -1
        else:
            if cur_coor[1] == 0:
                y_dir = 1
            if y_dir == -1:
                d_y = cur_coor[1]
            else:
                d_y = lim_y - cur_coor[1]

        cur_coor = [cur_coor[0] + x_dir * min(d_x, d_y), cur_coor[1] + y_dir * min(d_x, d_y)]
        if in_hole(board, cur_coor):
            break
        print("{} ({}, {})".format(define_side(board, cur_coor), *cur_coor))
    print("{} ({}, {})".format(define_hole(board, cur_coor), *cur_coor))

y, x = int(input()), int(input())

board = [[0, 0],
     [0, y],
     [x, 0], 
     [x, y]]

shoot(board, x, y)