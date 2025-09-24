# 배추가 심어져 있는 부분 확인 dfs 로 쭉쭉쭉 확인하고 len 해주면 확인 가능 
# ans [] for i for j ans.append(dfs(i, j)) -> len(ans) 정답!!
# T 받고, 가로  세로 받고 일단 다 0으로 하고 for loop 돌리면서 graph -> (x,y) append -> def dfs(x ,y)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())


def dfs(x, y):
    graph[x][y] = 0
    count = 1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    return count

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    moves = [(1,0), (-1,0), (0,1), (0, -1)]

    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1

    ans = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                ans.append(dfs(i, j))
    print(len(ans))
