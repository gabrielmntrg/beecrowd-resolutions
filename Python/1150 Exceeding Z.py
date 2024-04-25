x = int(input())
z = x-1
s = x
count = 1
while z <= x:
    z = int(input())

while s < z:
    s += x + count
    count += 1

print(count)