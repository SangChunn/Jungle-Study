import math
from sys import stdin

n, m = map(int, stdin.readline().split())

A= (math.comb(n,m))
print(A)
