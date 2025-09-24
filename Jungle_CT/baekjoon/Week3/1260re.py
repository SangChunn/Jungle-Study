import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True

def bfs(start):
    q = deque([start])
    dist = [-1] * (N+1)
    dist[start] = 0
    while q:
        v = q.popleft()
        print(v, end =' ')
        for nxt in graph[v]:
            if dist[nxt] == -1:
                dist[nxt] = dist[v] + 1
                q.append(nxt)
bfs(1)