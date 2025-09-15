import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
out = []
check = [False] * (N + 1)

def recur(depth):
    if depth == M:
        out.append(' '.join(map(str, rs)))  # 완성된 한 줄을 리스트로 반환
        return
    for i in range(1, N + 1):
        if not check[i]:
            check[i] = True
            rs.append(i)
            recur(depth + 1) # 자식이 돌려준 결과를 누적
            rs.pop()
            check[i] = False
    return out

recur(0)
print('\n'.join(out))