#AB 를 먼저 곱하면 AB 에서 같은 숫자는 한번만 곱하고 그 뒤  A,B 에서 중복된 숫자 제외하고 똑같이 C랑도 해주기

import sys
input = sys.stdin.readline

INF = 10**18
N = int(input())
num = [list(map(int , input().split()))for _ in range(N)]
p = [num[0][0]] + [num[i][1] for i in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]
#i[0] * i[1] * i+1[1] , i[0] * i+1[1] * i+2[1]
for length in range(2, N+1):          # 구간 길이
    for i in range(1, N - length + 2):  # 구간 시작
        j = i + length - 1             # 구간 끝
        dp[i][j] = INF
        for k in range(i, j):          # 분할 지점
            cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[1][N])