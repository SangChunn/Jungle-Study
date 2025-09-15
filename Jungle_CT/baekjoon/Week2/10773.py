from sys import stdin

K = int(stdin.readline())
stack = []

for _ in range(K):
    x = int(stdin.readline())
    if x == 0:
        if stack:
            stack.pop()
    else:
        stack.append(x)

print(sum(stack))