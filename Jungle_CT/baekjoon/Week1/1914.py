from sys import stdin
N = int(stdin.readline())
def hanoi(N, x, y, z):
    if N == 1:
        print (x, z)
    else:
        hanoi(N-1, x, z, y)
        print(x, z)
        hanoi(N-1, y, x, z)
print(2**N-1)
if N<=20:
    hanoi(N, 1, 2, 3)