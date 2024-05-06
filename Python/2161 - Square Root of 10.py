def ten_square(n):
    result = 0
    for i in range(n):
        result += 6
        result = 1 / result
    return result + 3

n = int(input())
print(f'{ten_square(n):.10f}')