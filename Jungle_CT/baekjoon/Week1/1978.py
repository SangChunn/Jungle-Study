N = int(input())
case = list(map(int, input().split()))
sum = 0

for i in case:
    if i == 1:
        continue
    for n in range(2, i):
        if (i%n == 0):
            break
    else:
        sum += 1
print(sum)