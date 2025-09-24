from collections import deque
V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
indegree = [0] * (V+1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree += 1

def topology():
    result = []
    q = deque()

    for i in range(1, V+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")