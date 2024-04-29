n = int(input())

for _ in range(n):
    x = int(input())
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    if s == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')