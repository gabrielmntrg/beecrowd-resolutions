inputs = list(map(int, input().split()))
a = inputs[0]; inputs.pop(0) 
for i in inputs: 
    if i > 0: n = i
s = 0

for i in range(n):
    s += a + i

print(s)