def euclidean(a, b):
    if b == 0:
        return a
    else:
        return euclidean(b, a % b)

while True:
    try:
        a, b, c = map(int, input().split())

        if c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == b**2 + c**2:
            if euclidean(a, b) == 1 and euclidean(b, c) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')

    except EOFError:
        break