import sys
input = sys.stdin.readline

N, M =  map(int, input().split())

rs = []
total = []
check = [False] * (N + 1)

def back(start, depth):
    if depth == M:
        return total.append(' '.join(map(str, rs)))
    for i in range(start, N+1):
        if check[i] == False:
            rs.append(i)
            back(start, depth+1)
            rs.pop()

back(1, 0)
print('\n'.join(total))