x = int(input())
odds = 0

while odds < 6:
    if x % 2 != 0:
        print(x)
        odds += 1
    x += 1