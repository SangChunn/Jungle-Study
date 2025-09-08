from sys import stdin

N = int(stdin.readline())

def factorial(N):
    if N > 0:
        return N * factorial(N-1)
    else:
        return 1
print(factorial(N))