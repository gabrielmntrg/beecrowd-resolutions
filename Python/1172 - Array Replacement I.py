array = [int(input()) for i in range(10)]

for i in range(10):
    array[i] = 1 if array[i] <= 0 else array[i]

for i in range(10):
    print(f"X[{i}] = {array[i]}")