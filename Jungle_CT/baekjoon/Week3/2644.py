# n 에 모든 사람 두번째줄에는 구해야되는 촌수, m 은 # edge 4번째부터는 x,y 트리형식
import sys
input = sys.stdin.readline
n = int(input())
q, w = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (n+1)
ans = -1
def dfs(v, d):
    global ans
    if v == w:
        ans = d
        return
    visited[v] =True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, d+1)

dfs(q, 0)
print(ans)