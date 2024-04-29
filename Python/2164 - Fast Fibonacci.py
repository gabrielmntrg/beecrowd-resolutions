def binet(n):
    return (((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n)/(5**0.5)

n = int(input())
print(f'{binet(n):.1f}')