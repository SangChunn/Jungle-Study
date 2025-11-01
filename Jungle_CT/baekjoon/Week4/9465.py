import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [
        list(map(int, input().split())),  
        list(map(int, input().split()))
    ] 

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    v0, v1 = dp[0][1], dp[1][1]     
    dp[0][1] = v0 + dp[1][0]
    dp[1][1] = v1 + dp[0][0]

    for i in range(2, n):
        v0, v1 = dp[0][i], dp[1][i]   #
        dp[0][i] = v0 + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = v1 + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][-1], dp[1][-1]))