evens = 0
odds = 0
positives = 0
negatives = 0

for i in range(5):
    n = int(input())
    
    if n % 2 == 0:
        evens += 1
    else:
        odds += 1

    if n > 0:
        positives += 1
    elif n < 0:
        negatives += 1

print(f"{evens} valor(es) par(es)")
print(f"{odds} valor(es) impar(es)")
print(f"{positives} valor(es) positivo(s)")
print(f"{negatives} valor(es) negativo(s)")