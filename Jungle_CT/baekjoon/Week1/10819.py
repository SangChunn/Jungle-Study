from sys import stdin
from itertools import permutations

N = int(stdin.readline())
num = list(map(int,stdin.readline().split()))
best=0
for p in permutations(num, N):
    s = sum(abs(p[i]-p[i+1]) for i in range(N-1))
    if s > best:
        best = s
print(best)