while True:
    try:
        v = float(input())
        d = float(input())
        r = d / 2
        height = v / (3.14 * r**2)
        area = 3.14 * r**2
        print(f"ALTURA = {height:.2f}\nAREA = {area:.2f}")

    except EOFError:
        break