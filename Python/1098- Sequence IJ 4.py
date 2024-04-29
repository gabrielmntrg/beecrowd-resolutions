def print_ij(i, j):
    if i == int(i):
        print(f'I={i:.0f}', end=' ')
    else:
        print(f'I={i:.1f}', end=' ')
    if j == int(j):
        print(f'J={j:.0f}')
    else:
        print(f'J={j:.1f}')

i, j = 0, 1
while i < 2.2:
    print_ij(i, j)
    print_ij(i, j+1)
    print_ij(i, j+2)
    i = round(i+0.2, 1)
    j = round(j+0.2, 1)