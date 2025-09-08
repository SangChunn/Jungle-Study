from sys import stdin

N = int(input())
num = list(int(stdin.readline()) for _ in range(N))
num.sort()


for x in num:
    print(x)