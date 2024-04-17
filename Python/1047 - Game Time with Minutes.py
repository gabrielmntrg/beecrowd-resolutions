initH, initM, finalH, finalM = map(int, input().split())

duratH = finalH - initH
duratM = finalM - initM

if initH == finalH and initM == finalM:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if duratM < 0:
        duratH -= 1
        duratM += 60

    if duratH < 0:
        duratH += 24

    print(f"O JOGO DUROU {duratH} HORA(S) E {duratM} MINUTO(S)")