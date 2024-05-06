def two_square(n):
    result = 0
    for i in range(n):
        result += 2
        result = 1 / result
    return result + 1

n = int(input())
print(f'{two_square(n):.10f}')