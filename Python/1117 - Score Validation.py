valid = 0
average = 0
while valid < 2:
    score = float(input())

    if score < 0 or score > 10:
        print('nota invalida')
    else:
        valid += 1
        average += score

print(f'media = {average / 2:.2f}')