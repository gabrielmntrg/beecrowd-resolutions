n = int(input())
s, b, a = 0, 0, 0
s1, b1, a1 = 0, 0, 0

for _ in range(n):
    name = input()
    
    inputs = list(map(int, input().split()))
    s += inputs[0]; b += inputs[1]; a += inputs[2]

    inputs = list(map(int, input().split()))
    s1 += inputs[0]; b1 += inputs[1]; a1 += inputs[2]

print(f'Pontos de Saque: {s1 / s * 100:.2f} %.')
print(f'Pontos de Bloqueio: {b1 / b * 100:.2f} %.')
print(f'Pontos de Ataque: {a1 / a * 100:.2f} %.')