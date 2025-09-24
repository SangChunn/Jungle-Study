import sys, heapq
input = sys.stdin.readline
INF = 1e8
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) 
s, fin = list(map(int , input().split()))
distance = [INF] * (N+1)
# dist 하나 갈떄 queue 에다가 다음 노드 넣어주고 w 넣어줘서 제일 작은 경우 뽑아주기
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
dijkstra(s)
print(distance[fin])