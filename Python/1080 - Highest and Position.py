n = int(input())
count = 1
highest = n

for i in range(99):
    n = int(input())
    count += 1
    if n > highest:
        highest = n
        position = count

print(highest)
print(position)