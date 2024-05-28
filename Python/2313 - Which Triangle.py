sizes = list(map(int, input().split()))
sizes.sort()

if sizes[2] < sizes[0] + sizes[1] and sizes[2] > abs(sizes[0] - sizes[1]):
    if sizes[0] == sizes[1] == sizes[2]:
        print("Valido-Equilatero")
    elif sizes[0] == sizes[1] or sizes[0] == sizes[2] or sizes[1] == sizes[2]:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")

    print("Retangulo:", end=" ")

    if sizes[0]**2 == sizes[1]**2 + sizes[2]**2 or sizes[1]**2 == sizes[0]**2 + sizes[2]**2 or sizes[2]**2 == sizes[0]**2 + sizes[1]**2:
        print("S")
    else:
        print("N")
else:
    print("Invalido")