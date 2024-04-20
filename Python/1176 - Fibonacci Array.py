def fibonacci(n):
    prev, curr = 0, 1
    for i in range(n):
        prev, curr = curr, prev + curr
    return prev

t = int(input())

for i in range(t):
    n = int(input())
    print(f'Fib({n}) = {fibonacci(n)}')