# 4
#0 10 15 20.     1이라는 도시에서 2로는 10 3으로는 15 4로는 20 그래서 갔던 idx는 이제 못가는거지 무조건 마지막에는 처음 시작한 idx로 돌아가는거고
#5 0 9 10
#6 13 0 12
#8 8 9 0
#그러면 처음 인덱스를 설정하고 그걸 못가게 하면서 permutaion 해야것네 아 ! 자기가 출발한 곳에 해당하는 인덱스를 그 뒤에 [0] 으로 넘기면 되잖 
from sys import stdin
from itertools import permutations

N = int(stdin.readline())
arr = [list(map(int,(stdin.readline().split())))for _ in range(N)]
##w[0][1] = 10
## w[1][2] = 9
start = 0
ans = float('inf') #무한대 설정
other = range(1, N)
for p in permutations(other): #other = range(1,4)   길이 3의 배열 생성, 정수로는 안되고 이터러블로 해야됨 int XXXXX
    cur = start #start = 0 고정 (굳이 안해도 되긴 함)
    cost = 0
    ok = True

    for next in p: #p = (1, 2, 3)
        w = arr[cur][next]
        if w == 0:
            ok = False
            break
        cost += w
        if cost >= ans: #전 순열보다 크기가 크면 예 안되겠죠
            ok = False  
            break
        cur = next
    if not ok:
        continue
    w = arr[cur][start]
    if w == 0:
        continue
    cost += w
    if cost<ans:
        ans = cost
print(ans)