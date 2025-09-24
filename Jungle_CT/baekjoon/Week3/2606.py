import sys
input = sys.stdin.readline

N = int(input())
E = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(sum(visited) - 1)