a, b, c = map(int, input().split())
array = sorted([a, b, c])

print(*array, sep="\n")
print()
print(a, b, c, sep="\n")