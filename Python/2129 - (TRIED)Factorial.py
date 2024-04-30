# Não foi aceito :( TLE

def without_zeros(n):
    while n % 10 == 0:
        n //= 10
    return n

def factorial(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

k = 1
while True:
    try:
        n = int(input())
        result = without_zeros(factorial(n))
        
        print(f'Instancia {k}')
        print(result % 10)
        k += 1
    except EOFError:
        break