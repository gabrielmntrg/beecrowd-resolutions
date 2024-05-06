n = int(input())
wins = n

for i in range(n):
    k = input()
    if 'CD' in k:
        wins -= 1

print(wins)