import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())  
board = [input().strip() for _ in range(R)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]

ans = 1
def dfs(r, c, used):
    global ans
    ans = max(ans, len(used))
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            ch = board[nr][nc]
            if ch not in used:
                used.add(ch)           # ✅ 새 set 만들지 않고 직접 추가
                dfs(nr, nc, used)
                used.remove(ch)        # ✅ 재귀가 끝나면 되돌리기(backtracking)

dfs(0, 0, {board[0][0]})
print(ans)