from sys import stdin
import itertools
import math

N = int(input())
total = 0
for i in range(N):
    a, *b = map(int,input().split())
    nCr = itertools.combinations(b, 2)
    for i in nCr:   
        comb = math.gcd(*i)
        total += comb
    print(total)
    total = 0 