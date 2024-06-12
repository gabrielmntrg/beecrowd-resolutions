n = int(input())
minimum = False
chosen = 0
chosenNote = 0

for _ in range(n):
    registration, note = map(float, input().split())
    if note >= 8:
        minimum = True
        if note > chosenNote:
            chosen = registration
            chosenNote = note

if minimum:
    print(int(chosen))
else:
    print("Minimum note not reached")