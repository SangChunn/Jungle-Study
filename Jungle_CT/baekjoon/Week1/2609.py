from sys import stdin

i, j = list(map(int, stdin.readline().split()))

def GCD(i ,j):
    if i % j == 0:
        return j
    elif j == 0:
        return i
    else:
        return GCD(j, i%j)
print(GCD(i, j))

def LCM(i, j):
    return i * j // GCD(i,j)

print(LCM(i, j))