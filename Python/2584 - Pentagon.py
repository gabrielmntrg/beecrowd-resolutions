from math import tan, pi

def cotan(n):
    return 1 / tan(n)

def pentagonal(n):
    return 5/4 * n**2 * cotan(pi/5)

c = int(input())
for i in range(c):
    n = int(input())
    area = pentagonal(n)
    print(f'{area:.3f}')