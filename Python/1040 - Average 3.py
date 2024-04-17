n1, n2, n3, n4 = map(float, input().split())
average = (n1*2 + n2*3 + n3*4 + n4) / 10

print(f"Media: {average:.1f}")
if average >= 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    average = (average + n5) / 2
    if average >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {average:.1f}")