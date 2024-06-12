n = int(input())

for _ in range(n):
    outlets = list(map(int, input().split()))
    result = abs(outlets[0] - 1 - sum(outlets[1:]))
    print(result)