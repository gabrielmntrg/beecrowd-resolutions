x = int(input())
y = int(input())
s = 0

if x > y:
    x, y = y, x

for i in range(x+1, y):
    if i % 2 != 0:
        s += i
print(s)