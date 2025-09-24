# * 2 or 1추가
import sys
from collections import deque
input = sys.stdin.readline
A, B = map(int, input().split())

def bfs(A, B):
    q = deque([(A, 1)])
    while q:
        num, cnt = q.popleft()
        if num == B:
            return cnt
        if num*2 <= B:
            q.append((num*2, cnt+1))
        if num*10 +1 <= B:
            q.append((num*10+1, cnt+1))
    return -1
print(bfs(A, B))