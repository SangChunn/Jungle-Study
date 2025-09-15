from sys import stdin

stack = []
N = int(stdin.readline())

for _ in range(N):
    order = stdin.readline().strip()

    if "push" in order:
        num = int(order.split()[1])
        stack.append(num)
    elif "pop" in order:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in order:
        print(len(stack))
    elif "empty" in order:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "top" in order:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
