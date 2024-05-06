def unlucky(n):
    return True if '13' in str(n) else False

n = int(input())
if unlucky(n):
    print(f'{n} es de Mala Suerte')
else:
    print(f'{n} NO es de Mala Suerte')