n = int(input())
inn = 0
out = 0

for _ in range(n):
    x = int(input())

    if x >= 10 and x <= 20:
       inn += 1
    else:
        out += 1

print(f'{inn} in\n{out} out')