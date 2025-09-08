#(10,8), (0,a) ,(0, b) 이렇게나오면 나눠보자 일단 0-a b-a 8-b 순차적 
#(1,4) -> 4-0 8-4 그리고 다 곱해주기 그리고 max 출력하면 끝!!!!! 근데 구현을 하는게 귀찮아
#허걱 그러면 만약에 여러번 자를떄는 안에 index를 크기순서로 정렬해주고 하나하나 뺴주고 뺴주고 하면 되겠네
x, y = list(map(int, input().split()))
num = int(input())
cut_y = [0, y]
cut_x = [0, x]
cut_list = [list(map(int, (input().split()))) for _ in range(num)]

for i, j in cut_list:
    if i == 0:
        cut_y.append(j)
    elif i == 1:
        cut_x.append(j)

cut_y.sort()
cut_x.sort()
max_y = max(cut_y[i+1] - cut_y[i] for i in range(len(cut_y) -1))
max_x = max(cut_x[i+1] - cut_x[i] for i in range(len(cut_x) - 1))
print(max_y * max_x)