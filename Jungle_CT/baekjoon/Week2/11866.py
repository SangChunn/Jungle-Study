# 1 2 3 4 5 6 7 -> 3 6 2 7 그러면 팝해서 빼버리자 그전에건 popleft 하고 다시 append 
from sys import stdin
from collections import deque
N, K  = map(int, stdin.readline().split())
ans = []
myqueue = deque()
for i in range(1, N+1):
    myqueue.append(i)

while len(myqueue) > 1:
    for _ in range(K-1):
        myqueue.append(myqueue[0])
        myqueue.popleft()
    ans.append(myqueue[0])
    myqueue.popleft()
ans.append(myqueue[0])
print('<' + ', '.join(map(str, ans)) + '>')