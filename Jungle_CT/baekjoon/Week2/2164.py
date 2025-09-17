from sys import stdin
from collections import deque

N = int(stdin.readline())
myqueue = deque()

for i in range(1, N+1):
    myqueue.append(i)

while len(myqueue) > 1:
    myqueue.popleft()
    myqueue.append(myqueue.popleft())

print(myqueue[0])