def euclidean(a, b):
    if b == 0:
        return a
    else:
        return euclidean(b, a % b)

n = int(input())

for i in range(n):
    f1, f2 = map(int, input().split())
    print(euclidean(f1, f2))