def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def super_prime(n):
    for i in str(n):
        i = int(i)
        if not prime(i):
            return False
    return True

while True:
    try:
        n = int(input())

        if prime(n):
            if super_prime(n):
                print('Super')
            else:
                print('Primo')
        else:
            print('Nada')
            
    except EOFError:
        break