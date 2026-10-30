def calc_F(n):
    return 50 + (n - 40) / 4

def calc_C(n):
    return 10 + (n - 40) / 7 

N = int(input())
print(f"temperatuur (Fahrenheit): {calc_F(N)}")
print(f"temperatuur (Celsius): {calc_C(N)}")
