# 다 써야되는건 아니야 그러면 ? 제일 작은걸로 가져가면 그것도 안되고 왜냐? 만약 10 20 30 이면 30보단 40이 더 좋으니깐

# list.sort = []
# for i in range(list):
#     i * len(list[N-i]) 대소비교 i-1*len(list[N-i+1])

import sys
input = sys.stdin.readline

N = int(input())
list = [int(input().strip()) for _ in range(N)]
list.sort()
ans = 0
for i, w in enumerate(list):
    ans = max(ans, w * (N - i))
print(ans)