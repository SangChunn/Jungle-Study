from sys import stdin

N = int(stdin.readline())   
num = list(map(int, stdin.readline().split()))
plus, minus, multiply, divide = list(map(int, stdin.readline().split()))
max1 = int(-1e9)
min1 = int(1e9)

def dfs(i, cur, p, m, mu, d):
    global max1, min1
    if i == N:
        if cur > max1: max1 = cur
        if cur < min1: min1 = cur
        return
    else:
        if p > 0:
            dfs(i+1 , cur+num[i], p-1, m, mu, d)
        if m > 0:
            dfs(i+1, cur-num[i], p, m-1, mu, d)
        if mu > 0:
            dfs(i+1, cur*num[i], p, m, mu-1, d)
        if d > 0:
            if cur < 0 :
                dfs(i+1, -((-cur) // num[i]),p, m ,mu, d-1)
            else:
                dfs(i+1, cur//num[i], p, m, mu, d-1)
dfs(1, num[0], plus, minus, multiply, divide)
print(max1)
print(min1)