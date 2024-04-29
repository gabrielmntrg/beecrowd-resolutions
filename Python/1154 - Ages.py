ages = 0
count = 0

while True:
    age = int(input())
    if age < 0:
        break
    else:
        ages += age
        count += 1

print(f'{ages/count:.2f}')