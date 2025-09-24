from collections import deque
import sys
input = sys.stdin.readline

K = int(input().strip())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    check = [-1] * (V + 1)   # -1: 미방문, 0/1: 두 색
    ok = True

    for s in range(1, V + 1):
        if check[s] != -1 or not ok:
            continue
        q = deque([s])
        check[s] = 0
        while q and ok:
            u = q.popleft()
            for w in graph[u]:
                if check[w] == -1:
                    check[w] = check[u] ^ 1    # 0/1 토글
                    q.append(w)
                elif check[w] == check[u]:
                    ok = False
                    break

    print("YES" if ok else "NO")
