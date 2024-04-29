t = int(input())
answers = list(map(int, input().split()))
count = 0

for i in answers:
    if i == t:
        count += 1

print(count)