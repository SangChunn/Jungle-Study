# N개 존재, 각 물건은 W, V -> 최대 K만큼 넣을 수 있는데 그 중 max V를 구해라
    # dp로 if 
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [ list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = bag[i - 1]    
    for j in range(1, K+1):
        if j < w:                   
            dp[i][j] = dp[i - 1][j]
        else:                           
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[N][K])
