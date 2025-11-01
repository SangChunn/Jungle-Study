import sys
input = sys.stdin.readline
n = int(input())
def fibo(n):
    if n <= 1:
        return n
    i = 0
    j = 1
    for _ in range(0, n-1):
        nxt = i + j
        i = j
        j = nxt
    return nxt
print(fibo(n))