# Não foi aceito :( TLE

def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

while True:
    try:
        n, m = map(int, input().split())
        print(fib(fib(n)) % m)
    except EOFError:
        break 