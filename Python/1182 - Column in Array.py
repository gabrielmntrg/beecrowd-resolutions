m = []
column = int(input())
operation = input()
result = 0

for i in range(12):
    m.append([])
    for j in range(12):
        m[i].append(float(input()))

result = sum(m[i][column] for i in range(12))

if operation == 'S':
    print(f'{result:.1f}')
else:
    print(f'{result / 12:.1f}')