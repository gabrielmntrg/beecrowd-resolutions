matrix = []
operation = input()
result = 0

for i in range(12):
    matrix.append([])
    for j in range(12):
        matrix[i].append(float(input()))

for i in range(1, 12):
    for j in range(0, i):
        result += matrix[i][j]

if operation == 'M':
    result /= 66.0

print(f"{result:.1f}")