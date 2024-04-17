a, b, c = map(int, input().split())

# max(a, b, c)
g = int((a + b + abs(a-b)) / 2)
g = c if c>g else g
print(f"{g} eh o maior")