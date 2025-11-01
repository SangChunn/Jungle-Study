# dp 에 저장해놓고 \
# i-1 > i -> dp[i] = sum(dp[i-1] + dp[i])

import sys
input = sys.stdin.readline

N = int(input())
list = list(map(int, input().split()))
dp = [0] * N
dp[0] = list[0]
for i in range(1, N):
    dp[i] = max(list[i], dp[i-1] + list[i])
print(max(dp))