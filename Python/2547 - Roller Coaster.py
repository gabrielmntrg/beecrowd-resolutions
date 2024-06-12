while True:
    try:
        n, aMin, aMax = map(int, input().split())
        count = 0

        for _ in range(n):
            a = int(input())
            if a >= aMin and a <= aMax:
                count += 1

        print(count)
    except EOFError:
        break