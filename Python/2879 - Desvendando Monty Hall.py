n = int(input())
wins = 0

for _ in range(n):
    car = int(input())
    if car != 1:
        wins += 1

print(wins)