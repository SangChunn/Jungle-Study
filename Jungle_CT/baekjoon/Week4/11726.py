import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
if n== 1:
    print(1)
if n == 2:
    print(2)
if n >= 3:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    print(dp[n])