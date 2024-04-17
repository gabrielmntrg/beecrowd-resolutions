x = 1
while True:
    try:
        n = int(input())
        numbers = []

        for i in range(n+1):
            if i != 0:
                numbers.extend([i] * i)
            else:
                numbers.append(0)

        if len(numbers) == 1:
            print(f"Caso {x}: {len(numbers)} numero")
        else:
            print(f"Caso {x}: {len(numbers)} numeros")
        print(*numbers, sep=" ")
        print('')

        x += 1
    except EOFError:
        break