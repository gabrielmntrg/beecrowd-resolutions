correct = 2002
password = 0

while True:
    password = int(input())
    if password == correct:
        break
    else:
        print('Senha Invalida')

print('Acesso Permitido')