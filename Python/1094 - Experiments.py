total = 0
rabbits = 0
rats = 0
frogs = 0

n = int(input())
for i in range(n):
    temp = input().split()

    if temp[1] == 'C':
        rabbits += int(temp[0])
    if temp[1] == 'R':
        rats += int(temp[0])
    if temp[1] == 'S':
        frogs += int(temp[0])

    total += int(temp[0])

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {rabbits}')
print(f'Total de ratos: {rats}')
print(f'Total de sapos: {frogs}')
print(f'Percentual de coelhos: {rabbits/total*100:.2f} %')
print(f'Percentual de ratos: {rats/total*100:.2f} %')
print(f'Percentual de sapos: {frogs/total*100:.2f} %')