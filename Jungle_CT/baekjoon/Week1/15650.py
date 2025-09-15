import sys
input = sys.stdin.readline
N, M = map(int,input().split())

rs = []
total = []
check = [False] * (N+1)

def recur(start, depth):
    if depth == M:
        return total.append(' '.join(map(str, rs)))
    for i in range(start, N+1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            recur(i+1, depth+1)
            rs.pop()
            check[i] = False

recur(1, 0)
print('\n'.join(total))
