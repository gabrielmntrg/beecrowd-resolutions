t = int(input())
c = 0

for _ in range(t):
    c += 1
    team = list(map(int, input().split()))
    middleIndex = len(team) // 2
    print(f'Case {c}: {team[middleIndex]}')