# 1은 무조건 끝점 , 중간은 무조건 0으로만 
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(input().strip())
A = [' '] + A
total = 0
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    if A[u] == '1' and A[v] == '1':
        total += 1

#print(graph)

visited = [False] * (N+1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    k = 0

    while q:
        u = q.popleft()
        for w in graph[u]:
            if A[w] == '1':
                k += 1
            else:
                if not visited[w]:
                    visited[w] = True
                    q.append(w)
    return k
ans = 0
ans += 2 * total
for v in range(1, N+1):
    if A[v] == '0' and not visited[v]:
        k = bfs(v)
        ans += k*(k-1)
print(ans)