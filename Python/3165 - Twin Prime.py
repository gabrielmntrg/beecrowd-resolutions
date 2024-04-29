def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

while True:
    if prime(n) and prime(n - 2):
        print(n-2, n)
        break
    n -=1