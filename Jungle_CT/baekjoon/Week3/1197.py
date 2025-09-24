import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
parent = list(range(V + 1))
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key = lambda x : x[2])
result = 0

def find(x):
    if parent[x] == x:                               
        return x
    parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    x = find(x)
    y = find(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(E):
    x, y, C = edges[i]
    if find(x) != find(y):
        union(x, y)
        result += C

print(result)