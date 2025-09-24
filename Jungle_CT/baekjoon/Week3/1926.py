import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]
def dfs(x, y):
    graph[x][y] = 0
    count = 1
    for dx, dy in moves:
        nx, ny = x + dx , y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    return count
ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans.append(dfs(i, j))
if ans:
    print(len(ans))
    print(max(ans))
else:
    print(0)
    print(0)