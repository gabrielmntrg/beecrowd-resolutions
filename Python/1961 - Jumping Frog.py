p, n = map(int, input().split())
pipes = list(map(int, input().split()))
win = True

for i in range(len(pipes) - 1):
    if abs(pipes[i] - pipes[i+1]) > p:
        win = False
        break

print('YOU WIN' if win else 'GAME OVER')