def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

n = int(input())
for i in range(n):
    if i == n-1:
        print(fibonacci(i))
    else:
        print(fibonacci(i), end=' ')