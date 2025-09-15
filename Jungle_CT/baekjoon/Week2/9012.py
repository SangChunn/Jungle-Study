from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    s = stdin.readline().strip()
    stack = []
    ok = True
    for ch in s:
        if ch == '(':
            stack.append('(')
        else:
            if not stack:
                ok = False
                break
            stack.pop()
    print('YES' if ok and not stack else 'NO')