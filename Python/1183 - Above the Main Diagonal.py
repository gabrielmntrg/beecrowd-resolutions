matrix = []
operator = input()
result = 0

for i in range(12):
    matrix.append([])
    for j in range(12):
        matrix[i].append(float(input()))

for i in range(11):
    for j in range(i+1, 12):
        result += matrix[i][j]

if operator == 'M':
    result /= 66.0

print(f"{result:.1f}")