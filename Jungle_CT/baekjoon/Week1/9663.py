from sys import stdin

N = int(stdin.readline())

v1 = [0] * N
v2 = [0]* 2*N
v3 = [0] * 2*N
ans = 0
def dfs(i):
	global ans
	if i == N:
		ans += 1
		return
	for j in range(N):
		if v1[j] == v2[i+j] == v3[i-j] == 0:
				v1[j] = v2[i+j] = v3[i-j] = 1
				dfs(i+1)
				v1[j] = v2[i+j] = v3[i-j] = 0
dfs(0)
print(ans)