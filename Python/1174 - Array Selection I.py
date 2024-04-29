array = [float(input()) for i in range(100)]

for i in range(100):
    if array[i] <= 10:
        print(f"A[{i}] = {array[i]:.1f}")