import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
reverse_a = a[::-1]
dp1 = [0] * N
dp2 = [0] * N

dp1[0] = a[0]
for i in range(1, N):
    dp1[i] = max(a[i], dp1[i-1] + a[i])
dp2[0] = reverse_a[0]
for j in range(1, N):
    dp2[j] = max(reverse_a[j], dp2[j-1]+reverse_a[j])
dp2 = dp2[::-1]

result = max(dp1)

for k in range(1, N-1):
    result = max(result, dp1[k-1] + dp2[k+1])
print(result)