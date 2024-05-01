while True:
    x = int(input())
    evens = 0
    result = 0
    if x == 0: break

    while evens < 5:
        if x % 2 == 0:
            evens += 1
            result += x
        x += 1
    print(result)