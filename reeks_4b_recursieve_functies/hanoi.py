def step(depth, fr, to, extra):
    if depth == 1:
        print(f"Schijf {depth} van {fr} naar {to}")
        return 1
    step(depth - 1, fr, extra, to)
    print(f"Schijf {depth} van {fr} naar {to}")
    step(depth - 1, extra, to, fr)

def hanoi(depth):
    step(depth, 'A', 'C', 'B')
    print(f"{2**depth - 1} stappen gedaan")

hanoi(4)