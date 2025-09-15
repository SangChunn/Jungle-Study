import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = blue = 0
stack = [(0, 0, N)]  # (x, y, n)

while stack:
    x, y, n = stack.pop()

    # 현재 n×n이 한 색인지 검사
    first = paper[x][y]
    uniform = True
    for i in range(x, x + n):
        # 조기 종료를 위해 한 줄이라도 다르면 바로 탈출
        if not uniform: break
        for j in range(y, y + n):
            if paper[i][j] != first:
                uniform = False
                break

    if uniform:
        if first == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        # 4등분을 스택에 푸시 (순서는 상관없음)
        stack.append((x, y, half))                 # 좌상
        stack.append((x, y + half, half))          # 우상
        stack.append((x + half, y, half))          # 좌하
        stack.append((x + half, y + half, half))   # 우하

print(white)
print(blue)