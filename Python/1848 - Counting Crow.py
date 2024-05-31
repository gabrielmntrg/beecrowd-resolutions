screams = 0
number = 0

while screams < 3:
    dream = input()

    if dream == 'caw caw':
        screams += 1
        print(number)
        number = 0
    else:
        for i in range(len(dream)):
            if dream[i] == '*':
                number += 4 if i == 0 else 0
                number += 2 if i == 1 else 0
                number += 1 if i == 2 else 0