a, b, c = map(float, input().split())
[c, b, a] = sorted([a, b, c]) 

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c:
        print('TRIANGULO ISOSCELES')