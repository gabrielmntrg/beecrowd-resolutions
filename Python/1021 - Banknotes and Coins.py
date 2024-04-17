value = float(input())
value += 0.001
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("NOTAS:")
for i in notes:
    print(f"{int(value/i)} nota(s) de R$ {i:.2f}")
    value %= i

print("MOEDAS:")
for i in coins:
    print(f"{int(value/i)} moeda(s) de R$ {i:.2f}")
    value %= i