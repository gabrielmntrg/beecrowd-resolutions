cups = list(map(int, input().split()))

for i in cups:
    if i == 1:
        print(cups.index(i)+1)