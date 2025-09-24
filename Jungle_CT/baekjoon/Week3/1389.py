import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (N + 1)
    q = deque([start])
    dist[start] = 0
    total = 0
    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if dist[nxt] == -1:
                dist[nxt] = dist[v] + 1
                total += dist[nxt]
                q.append(nxt)
    return total

best_sum = float('inf')
best_node = 1
for node in range(1, N + 1):
    s = bfs(node)
    if s < best_sum:
        best_sum = s
        best_node = node

print(best_node)

def bfs(start):
    dist = [-1] * (N+1)
    q = deque([start])
    dist[start] = 0
    total = 0
    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if dist[nxt] == -1:
                dist[nxt] = dist[v] + 1