from sys import stdin, stdout

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

stack = []          # 인덱스만 저장 (0-based)
ans = [0] * N       # 각 탑의 정답

for i in range(N):  # i = 현재 탑의 0-based index
    # 현재 탑보다 높이가 작거나 같은 탑은 pop
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    # 스택에 남아있으면 가장 가까운 더 높은 탑의 번호
    ans[i] = stack[-1] + 1 if stack else 0   # 1-based 번호로 저장
    stack.append(i)  # 현재 탑의 index 저장

print(' '.join(map(str, ans)))