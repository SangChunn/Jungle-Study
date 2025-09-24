import sys
sys.setrecursionlimit(10**6)   ### 런타임 에러 안떠야됨
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()

parent = [0] * (N+1)   # 1~N+1

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)
dfs(1)
for i in range(2, N+1):
    print(parent[i])