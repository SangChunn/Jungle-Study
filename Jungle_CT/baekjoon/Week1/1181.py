from sys import stdin

N = int(stdin.readline())
text = list(set(stdin.readline().strip() for _ in range(N)))

text_sort = sorted(text)
#for i in range(N-1):
#    for j in range(N-1, i, -1):
#        if len(text_sort[j-1]) > len(text_sort[j]):
#            text_sort[j-1],text_sort[j] = text_sort[j], text_sort[j-1]
#for i in text_sort:
#    print(i)

## 버블정렬은 시간초과가 뜨네요 

text_total = sorted(text_sort, key=len)
for i in text_total:
    print(i)