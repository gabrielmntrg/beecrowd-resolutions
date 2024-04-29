t = int(input())
array = []

i = 0
while len(array) != 1000:
    array.append(i)
    if i < t-1:
        i+=1
    else:
        i = 0

for i in range(1000):
    print(f"N[{i}] = {array[i]}")