def factorial(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n

while True:
    try:
        m, n = map(int, input().split())
        print(factorial(m) + factorial(n))
    except EOFError:
        break