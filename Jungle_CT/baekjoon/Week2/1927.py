import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
numbers = PriorityQueue()
for i in range(N):
    num = int(input())
    if num == 0:
        if numbers.qsize()== 0:
            print(0)
        else:
            print(numbers.get())
    else:
        numbers.put(num)