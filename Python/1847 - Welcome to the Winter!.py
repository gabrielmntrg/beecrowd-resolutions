a, b, c = map(int, input().split())
ftc1 = b - a
ftc2 = c - b

if ftc1 < ftc2 or (ftc1 == ftc2 and ftc1 > 0 and ftc2 > 0):
    print(":)")
else:
    print(":(")