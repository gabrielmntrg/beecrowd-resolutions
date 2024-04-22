alcohol = 0
gasoline = 0
diesel = 0

while True:
    typ = int(input())
    if typ == 1:
        alcohol += 1
    elif typ == 2:
        gasoline += 1
    elif typ == 3:
        diesel += 1
    elif typ == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcohol}\nGasolina: {gasoline}\nDiesel: {diesel}')