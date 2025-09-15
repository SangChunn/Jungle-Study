from sys import stdin

N, C = map(int, stdin.readline().split())
house = [int(stdin.readline()) for _ in range(N)]
house.sort()

start, end = 1, house[-1] - house[0]
ans = 0
while start <= end:
    mid = (start + end) // 2  
    cnt = 1
    last = house[0]
    for i in range(1, N):
        if house[i] - last >= mid:
            cnt += 1
            last = house[i]
    if cnt >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid-1
print(ans)
