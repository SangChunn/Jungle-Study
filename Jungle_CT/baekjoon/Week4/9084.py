#1, 5, 10, 50, 100, 500
# test Case : T, sorted coin : N, price : M
# N 이 1, 2 이런 식으로 주어지고 그걸로 M 을 만드는 
# 1 1 1 1 1 1 1 1 1 1 
#         5         5
#                   10

#    5 10 15 20     35

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for c in coins: # 1, 2
        for i in range(c, M + 1):
            dp[i] += dp[i - c]

    print(dp[M])