inter = 0
gremio = 0
draws = 0
grenais = 0

while True:
    x, y = map(int, input().split())
    if x > y:
        inter += 1
    elif x < y:
        gremio += 1
    else:
        draws += 1
    grenais += 1
    print('Novo grenal (1-sim 2-nao)')
    x = int(input())
    if x == 2:
        break

print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{draws}')
if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')