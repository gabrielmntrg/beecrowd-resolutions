b, a, m, d = 0, 0, 0, 0

for i in range(int(input())):
    inputs = input().split()
    if inputs[1] == 'bonecos':
        b += int(inputs[2])
    elif inputs[1] == 'arquitetos':
        a += int(inputs[2])
    elif inputs[1] == 'musicos':
        m += int(inputs[2])
    else:
        d += int(inputs[2])

result = b//8 + a//4 + m//6 + d//12
print(result)