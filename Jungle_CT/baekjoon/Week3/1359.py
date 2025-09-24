import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())

#start = X, 1초면 -1 or +1, 순간이동 2*X
# u, v, w 이런식으로 될까?? -1 +1 2*X
INF = 10**9          # ✅ 큰 정수로
        # ✅ 넉넉한 최대 인덱스 (0~200000)
distance = [INF] * (200001)   # ✅ 배열 크기를 MAX+1

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for a, b in [(now*2, dist), (now+1, dist+1), (now-1, dist+1)]:
            if 0 <= a <= 199999 and distance[a] > b:
                distance[a] = b
                heapq.heappush(q, (b, a))
dijkstra(N)
print(distance[K])

# 내일은 DFS 죽이고 그리고 BFS 죽이고 그다음 위상정렬은 깔짝
