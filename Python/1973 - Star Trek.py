n = int(input())
stars = list(map(int, input().split()))
sheeps = sum(stars)
attackeds = [0] * n

i = 0
while i >= 0 and i < n:
    if stars[i] > 0:
        stars[i] -= 1
        attackeds[i] = 1
        sheeps -= 1
        i += 1 - 2 * (stars[i] % 2)
    else:
        i -= 1

print(sum(attackeds), sheeps)