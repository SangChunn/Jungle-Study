import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input().strip())
    p = [''] + list(map(int, input().split()))
    visited = [False] * (n+1)
    result = 0

    def dfs(v):
        visited[v] = True
        next = p[v]
        if not visited[next]:
            dfs(next)
            
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)