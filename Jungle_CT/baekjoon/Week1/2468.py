# 그러면 일단 N보다 작은 숫ㄷ자들을 다 0으로 바꾸고 나머지는 다 1로 바꾸고
# 1인것들만 찾아가면서 만약에 

from sys import stdin

N = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]
move = [[1,0], [-1,0], [0,1], [0,-1]]
max_h = max(map(max, arr))
def dfs(x, y, grid, visited):
    visited[x][y] = True
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= N:
            if not visited[nx][ny] and arr[nx][ny] > h:
                dfs(nx, ny, h ,visited)