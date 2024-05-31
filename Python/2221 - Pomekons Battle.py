t = int(input())

for _ in range(t):
    b = int(input())

    dabriel = list(map(int, input().split()))
    guarte = list(map(int, input().split()))

    vDabriel = (dabriel[0] + dabriel[1]) / 2
    vGuarte = (guarte[0] + guarte[1]) / 2

    if dabriel[2] % 2 == 0:
        vDabriel += b
    if guarte[2] % 2 == 0:
        vGuarte += b

    if vDabriel > vGuarte:
        print('Dabriel')
    elif vDabriel < vGuarte:
        print('Guarte')
    else:
        print('Empate')