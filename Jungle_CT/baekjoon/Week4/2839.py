import sys
input = sys.stdin.readline

N = int(input())
INF = 10**8
dp = [INF] * (N + 1)

if N >= 3: dp[3] = 1
if N >= 5: dp[5] = 1

for i in range(6, N + 1):
    if dp[i - 3] != INF:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if dp[i - 5] != INF:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[N] if dp[N] != INF else -1)