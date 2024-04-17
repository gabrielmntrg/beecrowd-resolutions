while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break

    if m > n:
        m, n = n, m

    for i in range(m, n+1):
        print(i, end=' ')
    print(f'Sum={sum(range(m, n+1))}')