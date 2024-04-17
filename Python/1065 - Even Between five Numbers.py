evens = 0

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        evens += 1

print(evens, "valores pares")