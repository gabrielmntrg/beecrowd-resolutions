a, b, c, d = map(int, input().split())
a, b, c, d = sorted([a, b, c, d])

if a < b+c and b < a+c and c < a+b:
    print('S')
elif b < c+d and c < b+d and d < b+c:
    print('S')
else:
    print('N')