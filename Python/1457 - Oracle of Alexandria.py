def factorial(n, k):
    if n <= 1:
        return 1
    return n * factorial(n - k, k)

t = int(input())
for _ in range(t):
    temp = input()
    k = temp.count('!')
    n = int(temp.replace('!', ''))
    print(factorial(n, k))