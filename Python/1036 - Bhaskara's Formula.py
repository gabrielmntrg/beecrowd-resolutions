from math import sqrt

a, b, c = map(float, input().split())
d = (b*b) - 4 * a * c

if d < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + sqrt(d)) / (2 * a)
    r2 = (-b - sqrt(d)) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")