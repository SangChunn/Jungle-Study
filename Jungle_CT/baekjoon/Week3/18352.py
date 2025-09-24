import sys
from collections import deque
input = sys.stdin.readline
N, M, K, X = map(int ,input().split())
graph = [[] for _ in  range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())      #단방향
    graph[u].append(v)

def bfs(start):
    q = deque([start])
    dist = [-1] * (N+1)   #거리 확인
    dist[start] = 0

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if dist[nxt] == -1:     
                dist[nxt] = dist[v] + 1
                q.append(nxt)
    return dist
distance = bfs(X)
ans = [i for i in range(1, N+1) if distance[i] == K]
print('\n'.join(map(str, ans)) if ans else -1)