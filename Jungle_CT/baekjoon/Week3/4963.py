# w, h input 받고 graph 크기 만들고
#  0 , 1 , 1 들어오는거 그대로 graph 에 넣고
# def dfs 구해주고 return len()
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

moves = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1, 1), (-1,-1)]

def dfs(x, y):
    graph[x][y] = 0 
    count = 1   
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    return count

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
        
    graph = []
    for i in range(h):
        a = list(map(int, input().split()))
        graph.append(a)
        
    ans = []
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                ans.append(dfs(i,j))
    print(len(ans))