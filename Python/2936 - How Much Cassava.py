portions = [300, 1500, 600, 1000, 150]
inputs = []
result = 0

for i in range(5):
    inputs.append(int(input()))

for i in range(5):
    result += inputs[i] * portions[i]

result += 225
print(result)