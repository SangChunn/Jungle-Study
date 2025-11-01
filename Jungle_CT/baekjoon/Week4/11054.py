#만약에 조건에 반례되는 인자가 나오면 거기서 count 를 끝내고 전에 있던 리스트들을 다 뺴고 그 부분부터 새로
#시작하면 되지 않을까요
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]
dp1 = [1] * N
dp2 = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if reverse_A[i] > reverse_A[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()
ans = 0
for i in range(N):
    ans = max(ans, dp1[i] + dp2[i] - 1)

print(ans)