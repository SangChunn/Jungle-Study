N = int(input())
num = [int(input().strip()) for _ in range(N)]
for i in range(len(num)-1):
    for j in range(len(num)-1, i, -1):
        if (num[j-1] > num[j]):
            num[j-1], num[j] = num[j], num[j-1]
for x in num:
    print(x)