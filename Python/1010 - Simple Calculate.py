code1, units1, price1 = map(float, input().split())
code2, units2, price2 = map(float, input().split())

total = (units1 * price1) + (units2 * price2)

print(f"VALOR A PAGAR: R$ {total:.2f}")