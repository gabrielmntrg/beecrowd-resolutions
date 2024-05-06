f1, f2 = map(float, input().split())
result = (100+f1) * (f2/100+1) - 100
print(f'{result:.6f}')