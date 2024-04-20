size = int(input())
array = list(map(int, input().split()))

print(f'Menor valor: {min(array)}')
print(f'Posicao: {array.index(min(array))}')