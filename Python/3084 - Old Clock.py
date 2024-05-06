while True:
    try:
        h, m = map(int, input().split())
        h /= 30
        m /= 6

        if h < 10:
            print(f'0{h:.0f}:', end='')
        else:
            print(f'{h:.0f}:', end='')

        if m < 10:
            print(f'0{m:.0f}')
        else:
            print(f'{m:.0f}')
    except EOFError:
        break