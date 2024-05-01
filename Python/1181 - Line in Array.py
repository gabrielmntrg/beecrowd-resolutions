line = int(input())
operation = input()

matrix = []
for i in range(12):
    matrix.append([])
    for j in range(12):
        matrix[i].append(float(input()))

result = sum(matrix[line][i] for i in range(12))
if operation == 'M':
    result /= 12

print(f'{result:.1f}')