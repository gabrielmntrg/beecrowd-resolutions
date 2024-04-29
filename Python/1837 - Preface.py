from math import ceil, floor

a, b = map(int, input().split())

if b < 0:
    q = ceil(a/b)
    b *= -1
    r = a % b
else:
    q = floor(a/b)
    r = a % b

print(q, r)