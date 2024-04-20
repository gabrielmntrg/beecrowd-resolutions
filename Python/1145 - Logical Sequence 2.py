x, y = map(int, input().split())
i = 1

while i <= y:
    for j in range(x):
        if j == x-1:
            print(i)
            i += 1
        else:
            print(i, end=' ')
            i += 1