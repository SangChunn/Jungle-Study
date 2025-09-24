#일단 첫째줄에 총 단지수 출력 -> 마지막에 graph에 남아있는거 다 sum?
# 처음 0하고 count 누적 nx ny dx dy 
# 마지막에 print 해 줄때 sort
import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y):
    graph[x][y] = 0
    count = 1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    return count
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans.append(dfs(i, j))
print(len(ans))
for v in sorted(ans):
    print(v)
