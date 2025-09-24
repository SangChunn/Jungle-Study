# total F , startlink = G, now = S, S -> G, U  up, D dow , (F, 1  넘어서면안됨)
import sys
from collections import deque
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
moves = []
if U != 0:
    moves.append(U)
if D != 0:
    moves.append(-D)
def bfs(start):
    q = deque([start])
    dist = [-1] * (F+1)
    dist[start] = 0
    while q:
        v = q.popleft()
        if v == G:
            return dist[v]
        for step in moves:
            nxt = v + step
            if 1<= nxt <= F and dist[nxt] == -1:
                dist[nxt] = dist[v] +1
                q.append(nxt)
    return -1
ans = bfs(S)
if ans == -1:
    print("use the stairs")
else:
    print(ans)