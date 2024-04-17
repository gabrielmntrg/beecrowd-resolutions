value = int(input())
notes = [100, 50, 20, 10, 5, 2, 1]

print(value)
for i in notes:
    print(f"{int(value/i)} nota(s) de R$ {i},00")
    value %= i