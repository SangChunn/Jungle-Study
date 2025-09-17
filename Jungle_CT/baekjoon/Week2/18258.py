from sys import stdin
from collections import deque

myqueue = deque()
N = int(stdin.readline())
for _ in range(N):
    order = stdin.readline().strip()

    if "push" in order:
        num = int(order.split()[1])
        myqueue.append(num)
    elif "pop" in order:
        if len(myqueue) == 0:
            print(-1)
        else:
            print(myqueue.popleft())
    elif "size" in order:
        print(len(myqueue))
    elif "empty" in order:
        if len(myqueue) == 0:
            print(1)
        else:
            print(0)
    elif "front" in order:
        if len(myqueue) == 0:
            print(-1)
        else:
            print(myqueue[0])
    elif "back" in order:
        if len(myqueue) == 0:
            print(-1)
        else:
            print(myqueue[-1])