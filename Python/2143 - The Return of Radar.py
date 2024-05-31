while True:
    t = int(input())
    if t == 0:
        break

    for _ in range(t):
        n = int(input())
        result = n*2-1 if (n%2) == 1 else n*2-2
        print(result)