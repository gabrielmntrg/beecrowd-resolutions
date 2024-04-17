start, end = map(int, input().split())
duration = end - start

if duration <= 0:
    duration += 24

print(f"O JOGO DUROU {duration} HORA(S)")