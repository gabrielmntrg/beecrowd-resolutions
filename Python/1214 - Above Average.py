c = int(input())

for i in range(c):
    averages = list(map(float, input().split()))
    average = sum(averages[1:]) / averages[0]
    above = 0
    
    size = averages[0]
    averages.pop(0)

    for i in averages:
        if i > average:
            above += 1

    print(f"{above / size * 100:.3f}%")