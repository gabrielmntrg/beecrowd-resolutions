array = [int(input())]

for i in range(1, 10):
    array.append(array[i-1] * 2)

for i in range(10):
    print(f"N[{i}] = {array[i]}")