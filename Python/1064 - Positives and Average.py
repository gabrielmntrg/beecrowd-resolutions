positives = 0
average = 0

for i in range(6):
    number = float(input())
    if number > 0:
        positives += 1
        average += number

average /= positives
print(f"{positives} valores positivos")
print(f"{average:.1f}")