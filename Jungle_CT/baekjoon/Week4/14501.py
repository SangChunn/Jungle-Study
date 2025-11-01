import sys
input = sys.stdin.readline

N = int(input())
list = []
for _ in range(N):
    t, p = map(int, input().split())
    list.append((t,p))
print(list)