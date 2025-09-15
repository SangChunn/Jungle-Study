from sys import stdin
N = int(stdin.readline())
stack = [int(stdin.readline()) for _ in range(N)]
count = 0
max_height = 0

while stack:                    # 스택이 빌 때까지 반복
    h = stack.pop()             # 맨 위(끝)에서 하나 꺼냄
    if h > max_height:          # 지금까지의 최대 높이보다 크면 보임
        count += 1
        max_height = h

print(count)