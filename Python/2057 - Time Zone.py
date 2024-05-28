s, t, f = map(int, input().split())
time = s + t + f

if time >= 24:
    print(time - 24)
elif time < 0:
    print(time + 24)
else:
    print(time)