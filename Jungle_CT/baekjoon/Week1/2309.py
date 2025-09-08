from sys import stdin

N = list(map(int,(stdin.readline().strip() for _ in range(9))))
def find():
    n = len(N)
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    for e in range(d+1, n):
                        for f in range(e+1, n):
                                for g in range(f+1, n):
                                    total = N[a] +N[b]+N[c]+N[d]+N[e]+N[f]+N[g]

                                    if total == 100:
                                        return (sorted([N[a],N[b],N[c],N[d],N[e],N[f],N[g]]))
    return
ans = find()
if ans:
    print(*ans, sep="\n")

#----------------------
   # ans = [7, 8, 10]

#print(ans)             # [7, 8, 10]  ← 리스트 그대로(대괄호/콤마 포함)
#print(*ans)            # 7 8 10      ← 요소를 각각 인자로 전달
#print(*ans, sep="\n")  # 7\n8\n10    ← 한 줄에 하나씩 출력
