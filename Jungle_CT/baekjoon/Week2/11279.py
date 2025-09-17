from sys import stdin
from queue import PriorityQueue

N = int(stdin.readline())
numbers = PriorityQueue()
for i in range(N):
    num = int(stdin.readline())
    if num == 0:
        if numbers.qsize() == 0:
            print(0)
        else :
            print(-numbers.get()) 
    else:
        numbers.put(-num) 

