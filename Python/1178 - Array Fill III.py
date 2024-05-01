n = []
n.append(float(input()))

for i in range(99):
    n.append(n[i] / 2)

for i in range(len(n)):
    print(f'N[{i}] = {n[i]:.4f}')