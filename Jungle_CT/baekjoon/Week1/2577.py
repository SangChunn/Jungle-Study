A = int(input())
B = int(input())
C = int(input())
total = A * B * C
m = str(total)
for x in range(10):
    print(m.count(str(x)))