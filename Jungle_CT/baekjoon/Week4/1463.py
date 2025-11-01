import sys
input = sys.stdin.readline
# N-1 % 3 == 0 -> 1    -> bottom-up -> first +1 , ->  N%2 == 0: -> min dp[i],dp[i//2] + 1
N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[N])