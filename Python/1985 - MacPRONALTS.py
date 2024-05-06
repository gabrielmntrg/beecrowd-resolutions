p = int(input())
total = 0

for _ in range(p):
    inputs = input().split()
    if inputs[0] == '1001':
        total += int(inputs[1]) * 1.50
    if inputs[0] == '1002':
        total += int(inputs[1]) * 2.50
    if inputs[0] == '1003':
        total += int(inputs[1]) * 3.50
    if inputs[0] == '1004':
        total += int(inputs[1]) * 4.50
    if inputs[0] == '1005':
        total += int(inputs[1]) * 5.50

print(f'{total:.2f}')