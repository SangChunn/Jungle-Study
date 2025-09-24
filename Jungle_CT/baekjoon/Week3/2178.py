import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    n, m = len(graph), len(graph[0])
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 1)])
    while queue:
        x, y, dist = queue.popleft()
        if x == end_x and y == end_y:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

print(bfs(0, 0, N-1, M-1, graph))