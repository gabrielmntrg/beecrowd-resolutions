temp = input().split()
w1 = int(temp[1])
temp = input().split()
x1 = int(temp[0]); y1 = int(temp[2]); z1 = int(temp[4])

temp = input().split()
w2 = int(temp[1])
temp = input().split()
x2 = int(temp[0]); y2 = int(temp[2]); z2 = int(temp[4])

init = z1 + (y1*60) + (x1*60*60) + (w1*60*60*24)
final = z2 + (y2*60) + (x2*60*60) + (w2*60*60*24)
durat = abs(final - init)

print(f'{durat // 86400} dia(s)'); durat %= 86400
print(f'{durat // 3600} hora(s)'); durat %= 3600
print(f'{durat // 60} minuto(s)'); durat %= 60
print(f'{durat} segundo(s)')