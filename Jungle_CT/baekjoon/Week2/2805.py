from sys import stdin
N, M = map(int, stdin.readline().split())
height = list(map(int, stdin.readline().split()))

start, end = 0, max(height)
result = 0                     

while start <= end:
    mid = (start + end) // 2
    total = 0
    for h in height:
        if h > mid:
            total += h - mid

    if total < M:             
        end = mid - 1
    else:                      
        result = mid           
        start = mid + 1

print(result)