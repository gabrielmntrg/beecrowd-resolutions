ages = list(map(int, input().split()))
middle = sorted(ages)[1]

print('huguinho' if middle == ages[0] else 'zezinho' if middle == ages[1] else 'luisinho')