n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    odds = 0
    result = 0
    
    while odds < y:
        if x % 2 != 0:
            result += x
            odds += 1
        x += 1
    print(result)