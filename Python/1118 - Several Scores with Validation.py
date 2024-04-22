valids = 0
average = 0

while True:
    score = float(input())
    if score < 0 or score > 10:
        print('nota invalida')
    else:
        average += score
        valids += 1

        if valids == 2:
            print(f'media = {average / 2:.2f}')
            valids = 0; average = 0
            
            while True:
                print('novo calculo (1-sim 2-nao)')
                x = int(input())
                if x == 1 or x == 2:
                    break
            if x == 2:
                break