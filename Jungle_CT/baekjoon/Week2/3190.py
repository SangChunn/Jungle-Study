from sys import stdin
from collections import deque

N = int(stdin.readline())
K = int(stdin.readline())

game = [[0]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int, stdin.readline().split())
    game[x-1][y-1] = 1
L = int(stdin.readline())
tr = []
for _ in range(L):
    t, r = stdin.readline().split()
    tr.append((int(t), r))
      
x, y = 0, 0
snake = deque([(x, y)])
direction = 0 
time = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not(0 <= nx < N and 0 <= ny < N):
        break
    if (nx, ny) in snake:
        break

    if game[nx][ny] == 1:
        game[nx][ny] = 0
        snake.append((nx, ny))
    else:
        snake.append((nx, ny))
        snake.popleft()
    
    if tr and time == tr[0][0]:
        _, rotation = tr.pop(0)
        if rotation == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
    x, y = nx, ny
print(time)