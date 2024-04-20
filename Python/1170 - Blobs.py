def blobs(x):
    if x <= 1:
        return 0
    else:
        return 1 + blobs(x / 2)

n = int(input())

for i in range(n):
    x = float(input())
    print(f'{blobs(x)} dias')