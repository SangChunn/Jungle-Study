import sys
sys.setrecursionlimit(10**6)  # 깊이 설정

pre = list(map(int, sys.stdin.read().split()))  #이렇게 받아오면 EOF 까지 한번에 쫙
n = len(pre)   # preorderㅇ 베열 
node = 0   
out = []    #다음 읽을 위치를 가리키는 전역 커서

def dfs(lo, hi):
    """
    전위순회 배열 pre를 node부터 읽어가며,
    (lo, hi) 범위에 들어가는 값들로만 서브트리를 구성해
    후위순서로 out에 담는다
    """
    global node
    if node >= n:
        return
    val = pre[node]
    if not (lo < val < hi):  
        return

    node += 1
    dfs(lo, val)   # 왼쪽: 값 < val
    dfs(val, hi)   # 오른쪽: 값 > val
    out.append(str(val))  # 후위순회: (왼 -> 오 -> 루트)

dfs(float("-inf"), float("inf"))
sys.stdout.write("\n".join(out))