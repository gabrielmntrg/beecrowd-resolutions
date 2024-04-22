def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    n = input()
    if n == '0':
        break
    result = 0
    size = len(n)
    for i in n:
        result += int(i) * factorial(size)
        size -= 1
    print(result)