salary = float(input())

if salary > 2000:
    earned = salary * 0.04
    salary += earned
    percentual = 4
elif salary > 1200:
    earned = salary * 0.07
    salary += earned
    percentual = 7
elif salary > 800:
    earned = salary * 0.10
    salary += earned
    percentual = 10
elif salary > 400:
    earned = salary * 0.12
    salary += earned
    percentual = 12
else:
    earned = salary * 0.15
    salary += earned
    percentual = 15

print(f"Novo salario: {salary:.2f}")
print(f"Reajuste ganho: {earned:.2f}")
print(f"Em percentual: {percentual} %")