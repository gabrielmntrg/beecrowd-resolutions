def prime(n):
    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

n = int(input())

for i in range(n):
    x = int(input())
    if prime(x):
        print('Prime')
    else:
        print('Not Prime')