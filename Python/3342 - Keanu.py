n = int(input())
area = n*n

if n % 2 == 0:
    print(f'{int(area/2)} casas brancas e {int(area/2)} casas pretas')
else:
    print(f'{int(area//2+1)} casas brancas e {int(area//2)} casas pretas')