n = int(input())

for _ in range(n):
    p1 = input()
    p2 = input()

    if p1 == 'ataque' and p2 == 'pedra':
        print('Jogador 1 venceu')
    if p1 == 'ataque' and p2 == 'papel':
        print('Jogador 1 venceu')
    if p1 == 'ataque' and p2 == 'ataque':
        print('Aniquilacao mutua')
    if p1 == 'pedra' and p2 == 'ataque':
        print('Jogador 2 venceu')
    if p1 == 'pedra' and p2 == 'papel':
        print('Jogador 1 venceu')
    if p1 == 'pedra' and p2 == 'pedra':
        print('Sem ganhador')
    if p1 == 'papel' and p2 == 'ataque':
        print('Jogador 2 venceu')
    if p1 == 'papel' and p2 == 'pedra':
        print('Jogador 2 venceu')
    if p1 == 'papel' and p2 == 'papel':
        print('Ambos venceram')