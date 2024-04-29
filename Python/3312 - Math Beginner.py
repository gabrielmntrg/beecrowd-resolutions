def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if prime(number):
        print(f'{number}! = {factorial(number)}')