evens = []
odss = []

for _ in range(15):
    x = int(input())
    if x % 2 == 0:
        evens.append(x)
    else:
        odss.append(x)

    if len(evens) == 5:
        for i in range(5):
            print(f'par[{i}] = {evens[i]}')
        evens = []
    if len(odss) == 5:
        for i in range(5):
            print(f'impar[{i}] = {odss[i]}')
        odss = []

if odss:
    for i in range(len(odss)):
        print(f'impar[{i}] = {odss[i]}')

if evens:
    for i in range(len(evens)):
        print(f'par[{i}] = {evens[i]}')