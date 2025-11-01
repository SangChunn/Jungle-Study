import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input().strip()) for _ in range(N)]
print(A)
A_coin = A[::-1]
ans = 0
for i in range(N):
    if A_coin[i] <= K:
        ans += K // A_coin[i]
        now = K % A_coin[i]
        K = now
    if K == 0:
        break
print(ans)