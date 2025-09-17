from ast import While
import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
#10 20 30 40 50 60
# 30 70 110 -> 100 110 -> 210
# 무조건 작은걸 묶는게 이득일까  
numbers = PriorityQueue()
for i in range(N):
    num = int(input())
    numbers.put(num)

ans = 0
while numbers.qsize() > 1:
        a = numbers.get()
        b = numbers.get()
        s = a + b
        ans += s
        numbers.put(s)
print(ans)