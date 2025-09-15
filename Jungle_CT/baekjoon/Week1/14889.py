# i -> 
from sys import stdin

N = int(stdin.readline())
N_grid = [list(map(int, stdin.readline().split())) for _ in range(N)]
min_grid = 0
print(N_grid)
print(N_grid[1][1])
visited = [False] * N

def S_grid():
    ST = LT = 0
    for i in range(N):
        for j in range(i+1, N):
            if visited[i] and visited[j]:
                ST += N_grid[i][j] + N_grid[j][i]
            elif not visited[i] and not visited[j]:
                LT += N_grid[i][j] + N_grid[j][i]
    return abs(ST-LT)
def back(index, count):
    global min_grid
    if count == N//2:
        min_grid = min(a)
