from math import sqrt

def perfect_square(n):
    return sqrt(n) % 1 == 0

def is_fibonacci(n):
    return perfect_square(5*(n*n) + 4) or perfect_square(5*(n*n) - 4)

k = int(input())
cont, ans = 0, 0

i = 4
while cont != k:
    if not is_fibonacci(i):
        ans = i
        cont += 1
    i += 1
print(ans)