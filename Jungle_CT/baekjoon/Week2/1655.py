import sys, heapq
input = sys.stdin.readline

N = int(input())
left = []   # 최대 힙 (음수)
right = []  # 최소 힙

for _ in range(N):
    x = int(input())

    if not left or x <= -left[0]:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)
    if len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))
    elif len(left) - len(right) > 1:
        heapq.heappush(right, -heapq.heappop(left))

    print(-left[0])