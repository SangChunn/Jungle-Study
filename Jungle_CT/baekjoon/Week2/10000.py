from sys import stdin

N = int(stdin.readline())
events = []  # (x, typ)  typ: -1=왼쪽(L, 시작), +1=오른쪽(R, 끝)

for _ in range(N):
    x, r = map(int, stdin.readline().split())
    L, R = x - r, x + r
    events.append((L, -1))
    events.append((R, +1))

# 같은 x에서는 R(+1) 먼저, 그다음 L(-1)
events.sort(key=lambda e: (e[0], -e[1]))

# 스택에는 state만 저장
# state: 0=막 열림, 1=바로 직전에 같은 x에서 이어 붙음(연속 접함), -1=중간에 끊김(연속 아님)
stack = []
ans = 0
last_x = None

for x, typ in events:
    if not stack:
        # 비어있을 때는 무조건 새로 연다
        stack.append(0)
        last_x = x
        continue

    if typ == -1:  # 왼쪽(L) = 시작
        # 직전 이벤트와 같은 x면, 바로 이어 붙은 것 → top을 '연속 접함(1)'으로 승격
        if x == last_x:
            if stack[-1] != -1:
                stack[-1] = 1
        else:
            # 다른 x에서 열리면 top은 더 이상 연속 아님
            stack[-1] = -1
        stack.append(0)
        last_x = x

    else:  # 오른쪽(R) = 끝
        top = stack.pop()
        # 바로 직전 이벤트가 같은 x에서 일어난 닫힘이고(top==1),
        # 즉 '연속 접점' 상황이면 +2, 아니면 +1
        if top == 1 and x == last_x:
            ans += 2
        else:
            ans += 1
        last_x = x

# 바깥 영역 +1
print(ans + 1)