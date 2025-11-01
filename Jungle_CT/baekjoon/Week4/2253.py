import sys
input = sys.stdin.readline

N, M = map(int, input().split())
not_jump = set(int(input()) for _ in range(M))

INF = float('inf')
KMAX = int((2 * N) ** 0.5) + 2


dp = [[INF] * (KMAX + 1) for _ in range(N + 1)]
dp[1][0] = 0  

for i in range(2, N + 1):
    if i in not_jump:
        continue
    for k in range(1, KMAX + 1):
        prev = i - k
        if prev <= 0 or prev in not_jump:
            continue
        for d in (k - 1, k, k + 1):
            if 0 <= d <= KMAX and dp[prev][d] != INF:
                dp[i][k] = min(dp[i][k], dp[prev][d] + 1)

ans = min(dp[N])
print(ans if ans != INF else -1)