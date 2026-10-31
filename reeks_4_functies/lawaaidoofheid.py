def maximale_blootstelling(n):
    time = 28800
    if n < 80:
        return -1.0
    return time / 2 ** ((n - 80) // 3)