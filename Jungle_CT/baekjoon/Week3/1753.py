import sys, heapq
input = sys.stdin.readline
INF = 1e8
V, E = list(map(int, input().split()))
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
distance = [INF] * (V+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))
dijkstra(K)

# 출력: 시작 정점은 0, 도달 불가는 'INK'
output_lines = []
for node in range(1, V + 1):
    if node == K:
        output_lines.append('0')
    else:
        if distance[node] != INF:
            dist = str(distance[node])
        else:
            dist = 'INF'

        output_lines.append(dist)

print('\n'.join(output_lines))